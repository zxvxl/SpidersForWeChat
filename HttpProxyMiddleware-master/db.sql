DROP TABLE IF EXISTS `wx_spiders`;
CREATE TABLE `wx_spiders` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `wx_name` varchar(255) DEFAULT NULL,
  `wx_code` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `hrefs` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `pubtime` varchar(20) DEFAULT NULL,
  `content` varchar(5000) DEFAULT NULL,
  `createTime` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;