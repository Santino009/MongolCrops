/*
Navicat MySQL Data Transfer

Source Server         : database
Source Server Version : 50623
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50623
File Encoding         : 65001

Date: 2021-04-12 17:48:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for testtxt1
-- ----------------------------
DROP TABLE IF EXISTS `testtxt1`;
CREATE TABLE `testtxt1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_process` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testtxt1
-- ----------------------------
INSERT INTO `testtxt1` VALUES ('1', 'a222');
INSERT INTO `testtxt1` VALUES ('3', 'asdsfa');
INSERT INTO `testtxt1` VALUES ('5', '66');
INSERT INTO `testtxt1` VALUES ('6', 'aassssss');
INSERT INTO `testtxt1` VALUES ('7', 'aassssss');
INSERT INTO `testtxt1` VALUES ('8', 'adadadad');
INSERT INTO `testtxt1` VALUES ('9', 'avvv');
INSERT INTO `testtxt1` VALUES ('10', 'avvv');
INSERT INTO `testtxt1` VALUES ('11', 'aza');
INSERT INTO `testtxt1` VALUES ('12', 'az');
INSERT INTO `testtxt1` VALUES ('19', 'azzz');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', 'admin');
INSERT INTO `user` VALUES ('2', 'adad', 's');
INSERT INTO `user` VALUES ('3', 'sss', 'ad');
