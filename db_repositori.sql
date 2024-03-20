/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 100432 (10.4.32-MariaDB)
 Source Host           : localhost:3306
 Source Schema         : db_repositori

 Target Server Type    : MySQL
 Target Server Version : 100432 (10.4.32-MariaDB)
 File Encoding         : 65001

 Date: 20/03/2024 20:43:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for data_dokumen
-- ----------------------------
DROP TABLE IF EXISTS `data_dokumen`;
CREATE TABLE `data_dokumen`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `nip` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `type_dokumen` enum('file','url') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nama_dokumen` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `nama_file` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `nip`(`nip` ASC) USING BTREE,
  CONSTRAINT `data_dokumen_ibfk_1` FOREIGN KEY (`nip`) REFERENCES `data_dosen` (`nip`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of data_dokumen
-- ----------------------------
INSERT INTO `data_dokumen` VALUES (1, 'h78652', 'file', 'nilai', 'nilai.xls');
INSERT INTO `data_dokumen` VALUES (2, 'h78652', 'url', 'nilaiv2', 'drive/nilai.xls');

-- ----------------------------
-- Table structure for data_dosen
-- ----------------------------
DROP TABLE IF EXISTS `data_dosen`;
CREATE TABLE `data_dosen`  (
  `nip` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nama_lengkap` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `prodi_id` int NULL DEFAULT NULL,
  PRIMARY KEY (`nip`) USING BTREE,
  INDEX `prodi_id`(`prodi_id` ASC) USING BTREE,
  CONSTRAINT `data_dosen_ibfk_1` FOREIGN KEY (`prodi_id`) REFERENCES `data_prodi` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of data_dosen
-- ----------------------------
INSERT INTO `data_dosen` VALUES ('h76422', 'risu', 4);
INSERT INTO `data_dosen` VALUES ('h76782', 'bae', 4);
INSERT INTO `data_dosen` VALUES ('h78123', 'kafka', 2);
INSERT INTO `data_dosen` VALUES ('h78623', 'kiara', 2);
INSERT INTO `data_dosen` VALUES ('h78652', 'calli', 2);

-- ----------------------------
-- Table structure for data_prodi
-- ----------------------------
DROP TABLE IF EXISTS `data_prodi`;
CREATE TABLE `data_prodi`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `kode_prodi` char(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `nama_prodi` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of data_prodi
-- ----------------------------
INSERT INTO `data_prodi` VALUES (2, 'hi9s2', 'FMIPA');
INSERT INTO `data_prodi` VALUES (3, '239dq', 'asdjhw');
INSERT INTO `data_prodi` VALUES (4, NULL, 'kimia');
INSERT INTO `data_prodi` VALUES (5, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
