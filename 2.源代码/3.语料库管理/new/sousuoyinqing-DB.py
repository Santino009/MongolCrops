from flask import Flask, render_template, request, jsonify, session
import pymysql #与数据库连接
import settings
import json


def create_app():
    app = Flask(__name__, static_url_path='/static')  # 运用了python自带的微型框架flask
    app.config.from_pyfile('settings.py')    #_，找到app.py所在的目录，即默认为根目录。
    return app

app = create_app()
app.config['SECRET_KEY'] = "dagfrwagbfsegb"  #密钥

conn = pymysql.connect(         #连接我的mysql
    host=app.config['MYSQL_HOST'],#主机，app.config['MYSQL_HOST']的意思是，在settings.py文件里面找host
    port=app.config['MYSQL_PORT'],#端口
    user=app.config['MYSQL_USER'],
    passwd=app.config['MYSQL_PAW'],
    database=app.config['MYSQL_DB'],
    charset='utf8'

)
cursor = conn.cursor()#创建一个游标

@app.route('/')         #当前网址内执行以下操作
@app.route('/index', methods=['GET', 'POST']) #在装饰器app.route中传递methods参数改变请求方式
#get：获取 post：创建一个新的资源
def index():
    return render_template('index.html')    #制作网页 ##跳转到templates文件，返回index.html


@app.route('/get_data', methods=['POST'])
def get_data():         #搜索引擎与数据库连接
    request_data = json.loads(request.data)    #将已编码的JSON字符串解码为Python对象;该函数返回Python字段的数据类型
    page = int(request_data['page'])           #把json字符串转成字典
    wd = request_data['kw']   #kw是搜索框
    limit = app.config['PAGE_LIMIT']  #每页显示多少条语句，PAGE_LIMIT在setting里设置了
    cursor.execute(
        f'SELECT id, case_process FROM `testtxt` WHERE case_process LIKE "%{wd}%";')
    t = cursor.fetchall()   #fetchall()函数它的返回值是所有数据,也就是全部行记录  ##返回一行行带有关键词的语句
    ### t成为了存放关键词语句

    info = []  #空列表
    #start=(page - 1) * limit：表示每页起始位置
    #end=page * limit：表示每页结束位置
    #例子：page_data_list = data_list[start:end]
    for i in t[(page - 1) * limit: page * limit]:  #t[]列表
        info.append({
            #append() 方法用于在info[]列表末尾添加新的对象
            'id':i[0],
            'ctn':i[1]
        })


    datas = {
        'data': info,#'键'：值。值=关键词语句
        'count': len(t)#返回t列表的长度=返回的一行行带有关键词的语句=统计
    }
    return jsonify(datas)    #字典转成json字符串

# 请求登录界面
@app.route('/login_html')
def get_login():
    return render_template('login.html')

# 登录
@app.route('/login', methods=['POST'])
def login():
    # 获取poss请求数据的另一种方式
    username = request.form['username']  #request.form:获取以POST方式提交的数据（接收Form提交来的数据）
    password = request.form['password']

    print(f'select * from `user` where `username`="{username}"')
    cursor.execute(f'select * from `user` where `username`="{username}"')
    t = cursor.fetchone() #返回一个用户名记录
    msg = '' #msg表示一个空字符串
    # 没有查到该用户
    if not t:
        msg = '未找到该用户！请先注册！'
    # 查到用户信息
    else:
        # 账号 密码 匹配成功
        #id username passward
        #1  张三      1234
        #t[0] t[1] t[2]
        if password == t[2]:
            session['username'] = t[1]   #直接使用session对存储的内容赋值
            return render_template('index.html', username=t[1])#返回render_template模块
        else:
           msg = '用户名或密码错误！请重试！'
    return render_template('login.html', msg=msg)

# 注册
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']   #接收form表单提交来的数据
    password = request.form['password']
    cursor.execute(f'insert into user(username, password) values("{username}","{password}")')  #游标执行操作
    conn.commit()
    return render_template('login.html', msg="注册成功！请登录")

# 添加
@app.route('/add', methods=['POST'])
def add():
    request_data = json.loads(request.data) #将字符串转化为字典
    add_ctn = request_data.get('ctn') #获取ctn
    cursor.execute(f'insert into testtxt(case_process) values("{add_ctn}")')
    conn.commit()
    return {'msg':'添加成功'}

# 修改
@app.route('/modify', methods=['POST'])
def modify():
    request_data = json.loads(request.data)
    txt_id = int(request_data.get('id'))
    txt_ctn = request_data.get('ctn')
    cursor.execute(f'update testtxt set case_process="{txt_ctn}" where id={txt_id}')
    conn.commit()
    return {'msg':'修改成功'}

# 删除
@app.route('/delete', methods=['POST'])
def delete():
    request_data = json.loads(request.data)
    txt_id = int(request_data.get('id'))
    cursor.execute(f'delete from testtxt where id={txt_id}')
    conn.commit()
    return {'msg':'删除成功'}

# 退出登录
@app.route('/logout', methods=['POST'])
def logout():
    session['username'] = ''
    return ''

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
