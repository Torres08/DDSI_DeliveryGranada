-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: deliverydb
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add pedido',7,'add_pedido'),(26,'Can change pedido',7,'change_pedido'),(27,'Can delete pedido',7,'delete_pedido'),(28,'Can view pedido',7,'view_pedido'),(29,'Can add cliente',8,'add_cliente'),(30,'Can change cliente',8,'change_cliente'),(31,'Can delete cliente',8,'delete_cliente'),(32,'Can view cliente',8,'view_cliente'),(33,'Can add restaurante',9,'add_restaurante'),(34,'Can change restaurante',9,'change_restaurante'),(35,'Can delete restaurante',9,'delete_restaurante'),(36,'Can view restaurante',9,'view_restaurante'),(37,'Can add usuario',10,'add_usuario'),(38,'Can change usuario',10,'change_usuario'),(39,'Can delete usuario',10,'delete_usuario'),(40,'Can view usuario',10,'view_usuario'),(41,'Can add employee',11,'add_employee'),(42,'Can change employee',11,'change_employee'),(43,'Can delete employee',11,'delete_employee'),(44,'Can view employee',11,'view_employee'),(45,'Can add rating',12,'add_rating'),(46,'Can change rating',12,'change_rating'),(47,'Can delete rating',12,'delete_rating'),(48,'Can view rating',12,'view_rating'),(49,'Can add worktime',13,'add_worktime'),(50,'Can change worktime',13,'change_worktime'),(51,'Can delete worktime',13,'delete_worktime'),(52,'Can view worktime',13,'view_worktime'),(53,'Can add gasto',14,'add_gasto'),(54,'Can change gasto',14,'change_gasto'),(55,'Can delete gasto',14,'delete_gasto'),(56,'Can view gasto',14,'view_gasto'),(57,'Can add ingreso',15,'add_ingreso'),(58,'Can change ingreso',15,'change_ingreso'),(59,'Can delete ingreso',15,'delete_ingreso'),(60,'Can view ingreso',15,'view_ingreso'),(61,'Can add menu',16,'add_menu'),(62,'Can change menu',16,'change_menu'),(63,'Can delete menu',16,'delete_menu'),(64,'Can view menu',16,'view_menu'),(65,'Can add producto',17,'add_producto'),(66,'Can change producto',17,'change_producto'),(67,'Can delete producto',17,'delete_producto'),(68,'Can view producto',17,'view_producto'),(69,'Can add detalle pedido',18,'add_detallepedido'),(70,'Can change detalle pedido',18,'change_detallepedido'),(71,'Can delete detalle pedido',18,'delete_detallepedido'),(72,'Can view detalle pedido',18,'view_detallepedido'),(73,'Can add asigna',19,'add_asigna'),(74,'Can change asigna',19,'change_asigna'),(75,'Can delete asigna',19,'delete_asigna'),(76,'Can view asigna',19,'view_asigna'),(77,'Can add encarga',20,'add_encarga'),(78,'Can change encarga',20,'change_encarga'),(79,'Can delete encarga',20,'delete_encarga'),(80,'Can view encarga',20,'view_encarga');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$PH5FdpaFugHEKOj0Zxp6ql$PzbAT+nlh4OWL99xlfgRttailc3lkl+pf53kXd5h9Eg=','2024-01-14 13:56:22.466729',1,'mario','','','marioillan18@gmail.com',1,1,'2024-01-14 13:54:28.295605');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_asigna`
--

DROP TABLE IF EXISTS `delivery_asigna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_asigna` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pedido_id` bigint NOT NULL,
  `trabajador_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `delivery_asigna_trabajador_id_pedido_id_b2e8f03e_uniq` (`trabajador_id`,`pedido_id`),
  KEY `delivery_asigna_pedido_id_06640297_fk_delivery_pedido_id` (`pedido_id`),
  CONSTRAINT `delivery_asigna_pedido_id_06640297_fk_delivery_pedido_id` FOREIGN KEY (`pedido_id`) REFERENCES `delivery_pedido` (`id`),
  CONSTRAINT `delivery_asigna_trabajador_id_d5ceecf7_fk_delivery_employee_id` FOREIGN KEY (`trabajador_id`) REFERENCES `delivery_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_asigna`
--

LOCK TABLES `delivery_asigna` WRITE;
/*!40000 ALTER TABLE `delivery_asigna` DISABLE KEYS */;
/*!40000 ALTER TABLE `delivery_asigna` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_insert_asigna` BEFORE INSERT ON `delivery_asigna` FOR EACH ROW BEGIN
    IF EXISTS (SELECT 1 FROM delivery_asigna WHERE trabajador_id = NEW.trabajador_id AND pedido_id = NEW.pedido_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ya existe una asignación para este trabajador y pedido.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `delivery_cliente`
--

DROP TABLE IF EXISTS `delivery_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_cliente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) NOT NULL,
  `Telefono` varchar(9) NOT NULL,
  `Direccion` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_cliente`
--

LOCK TABLES `delivery_cliente` WRITE;
/*!40000 ALTER TABLE `delivery_cliente` DISABLE KEYS */;
INSERT INTO `delivery_cliente` VALUES (1,'Bar Paco','622414144','Calle Agustina De Aragón 3 1B'),(2,'Mario','639468882','Tercias'),(3,'Juan','123123123','Agustina de Aragón 12'),(4,'Juan','493599853','Chorreadero 4 1C');
/*!40000 ALTER TABLE `delivery_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_detallepedido`
--

DROP TABLE IF EXISTS `delivery_detallepedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_detallepedido` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int unsigned NOT NULL,
  `pedido_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `delivery_detallepedido_pedido_id_producto_id_9f8e3398_uniq` (`pedido_id`,`producto_id`),
  KEY `delivery_detallepedi_producto_id_5699a4fd_fk_delivery_` (`producto_id`),
  KEY `delivery_detallepedido_pedido_id_6a41214c` (`pedido_id`),
  CONSTRAINT `delivery_detallepedi_producto_id_5699a4fd_fk_delivery_` FOREIGN KEY (`producto_id`) REFERENCES `delivery_producto` (`id`),
  CONSTRAINT `delivery_detallepedido_pedido_id_6a41214c_fk_delivery_pedido_id` FOREIGN KEY (`pedido_id`) REFERENCES `delivery_pedido` (`id`),
  CONSTRAINT `delivery_detallepedido_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_detallepedido`
--

LOCK TABLES `delivery_detallepedido` WRITE;
/*!40000 ALTER TABLE `delivery_detallepedido` DISABLE KEYS */;
INSERT INTO `delivery_detallepedido` VALUES (2,1,2,1),(6,1,7,1);
/*!40000 ALTER TABLE `delivery_detallepedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_employee`
--

DROP TABLE IF EXISTS `delivery_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(30) NOT NULL,
  `Apellidos` varchar(30) NOT NULL,
  `Direccion` varchar(255) NOT NULL,
  `IBAN` varchar(25) NOT NULL,
  `Mail` varchar(30) NOT NULL,
  `Telefono` varchar(9) DEFAULT NULL,
  `disponible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `delivery_employee_IBAN_12371679_uniq` (`IBAN`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_employee`
--

LOCK TABLES `delivery_employee` WRITE;
/*!40000 ALTER TABLE `delivery_employee` DISABLE KEYS */;
INSERT INTO `delivery_employee` VALUES (1,'Mario','Illán','Tercias 14 1B','1233333333333333333333333','juanlu@gmail.com','639468882',1),(2,'Mario','Illán Valero','Tercias 14 1B','1231312312312311231231231','marioillan@correo.ugr.es','639468882',1);
/*!40000 ALTER TABLE `delivery_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_encarga`
--

DROP TABLE IF EXISTS `delivery_encarga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_encarga` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pedido_id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `delivery_encarga_usuario_id_pedido_id_78a51f68_uniq` (`usuario_id`,`pedido_id`),
  KEY `delivery_encarga_pedido_id_262938c1_fk_delivery_pedido_id` (`pedido_id`),
  CONSTRAINT `delivery_encarga_pedido_id_262938c1_fk_delivery_pedido_id` FOREIGN KEY (`pedido_id`) REFERENCES `delivery_pedido` (`id`),
  CONSTRAINT `delivery_encarga_usuario_id_50d0b64e_fk_delivery_` FOREIGN KEY (`usuario_id`) REFERENCES `delivery_usuario` (`cliente_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_encarga`
--

LOCK TABLES `delivery_encarga` WRITE;
/*!40000 ALTER TABLE `delivery_encarga` DISABLE KEYS */;
INSERT INTO `delivery_encarga` VALUES (5,7,3);
/*!40000 ALTER TABLE `delivery_encarga` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `antes_insertar_encarga` BEFORE INSERT ON `delivery_encarga` FOR EACH ROW BEGIN

    IF EXISTS (SELECT 1 FROM delivery_encarga WHERE usuario_id = NEW.usuario_id AND pedido_id = NEW.pedido_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No puede haber dos usuarios con el mismo pedido';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `delivery_gasto`
--

DROP TABLE IF EXISTS `delivery_gasto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_gasto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Importe` int NOT NULL,
  `Fecha` datetime(6) NOT NULL,
  `comentario` longtext,
  `employee_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `delivery_gasto_employee_id_8a654a20_fk_delivery_employee_id` (`employee_id`),
  CONSTRAINT `delivery_gasto_employee_id_8a654a20_fk_delivery_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `delivery_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_gasto`
--

LOCK TABLES `delivery_gasto` WRITE;
/*!40000 ALTER TABLE `delivery_gasto` DISABLE KEYS */;
/*!40000 ALTER TABLE `delivery_gasto` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `evitar_gasto_negativo` BEFORE INSERT ON `delivery_gasto` FOR EACH ROW BEGIN
    IF NEW.Importe < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se permiten gastos negativos';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `delivery_ingreso`
--

DROP TABLE IF EXISTS `delivery_ingreso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_ingreso` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Importe` int NOT NULL,
  `Fecha` datetime(6) NOT NULL,
  `comentario` longtext,
  `pedido_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `delivery_ingreso_pedido_id_93a6f0dc_uniq` (`pedido_id`),
  CONSTRAINT `delivery_ingreso_pedido_id_93a6f0dc_fk_delivery_pedido_id` FOREIGN KEY (`pedido_id`) REFERENCES `delivery_pedido` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_ingreso`
--

LOCK TABLES `delivery_ingreso` WRITE;
/*!40000 ALTER TABLE `delivery_ingreso` DISABLE KEYS */;
/*!40000 ALTER TABLE `delivery_ingreso` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `evitar_ingreso_negativo` BEFORE INSERT ON `delivery_ingreso` FOR EACH ROW BEGIN
    IF NEW.Importe < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se permiten ingresos negativos';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `delivery_menu`
--

DROP TABLE IF EXISTS `delivery_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_menu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `restaurante_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `delivery_menu_restaurante_id_f3b4325b_fk_delivery_` (`restaurante_id`),
  CONSTRAINT `delivery_menu_restaurante_id_f3b4325b_fk_delivery_` FOREIGN KEY (`restaurante_id`) REFERENCES `delivery_restaurante` (`cliente_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_menu`
--

LOCK TABLES `delivery_menu` WRITE;
/*!40000 ALTER TABLE `delivery_menu` DISABLE KEYS */;
INSERT INTO `delivery_menu` VALUES (1,1);
/*!40000 ALTER TABLE `delivery_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_pedido`
--

DROP TABLE IF EXISTS `delivery_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_pedido` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `estado` varchar(40) NOT NULL,
  `restaurante_id` bigint NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `precio_total` decimal(10,2) NOT NULL,
  `repartidor_id` bigint DEFAULT NULL,
  `usuario_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `delivery_pedido_restaurante_id_71e1fb02_fk_delivery_` (`restaurante_id`),
  KEY `delivery_pedido_repartidor_id_5371ae8b_fk_delivery_employee_id` (`repartidor_id`),
  KEY `delivery_pedido_usuario_id_eb3884e1_fk_delivery_` (`usuario_id`),
  CONSTRAINT `delivery_pedido_repartidor_id_5371ae8b_fk_delivery_employee_id` FOREIGN KEY (`repartidor_id`) REFERENCES `delivery_employee` (`id`),
  CONSTRAINT `delivery_pedido_restaurante_id_71e1fb02_fk_delivery_` FOREIGN KEY (`restaurante_id`) REFERENCES `delivery_restaurante` (`cliente_ptr_id`),
  CONSTRAINT `delivery_pedido_usuario_id_eb3884e1_fk_delivery_` FOREIGN KEY (`usuario_id`) REFERENCES `delivery_usuario` (`cliente_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_pedido`
--

LOCK TABLES `delivery_pedido` WRITE;
/*!40000 ALTER TABLE `delivery_pedido` DISABLE KEYS */;
INSERT INTO `delivery_pedido` VALUES (2,'Entregado',1,'2024-01-14 16:19:20.000000',0.00,NULL,NULL),(7,'En Preparación',1,'2024-01-15 11:45:08.000000',0.00,NULL,3);
/*!40000 ALTER TABLE `delivery_pedido` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `rellenar_encarga` AFTER INSERT ON `delivery_pedido` FOR EACH ROW BEGIN
       INSERT INTO delivery_encarga (pedido_id, usuario_id)
       VALUES (NEW.id, NEW.usuario_id);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `rellenar_asigna` AFTER INSERT ON `delivery_pedido` FOR EACH ROW BEGIN
    DECLARE repartidor_disponible_id INT;

    SELECT id INTO repartidor_disponible_id
    FROM delivery_employee
    WHERE disponible = TRUE
    LIMIT 1;
    
    IF repartidor_disponible_id IS NOT NULL THEN
        INSERT INTO delivery_asigna (pedido_id, trabajador_id)
        VALUES (NEW.id, repartidor_disponible_id);
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_delete_pedido` BEFORE DELETE ON `delivery_pedido` FOR EACH ROW BEGIN
    IF EXISTS (SELECT 1 FROM delivery_asigna WHERE pedido_id = OLD.id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se puede eliminar el pedido porque está asignado a un trabajador.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `delivery_producto`
--

DROP TABLE IF EXISTS `delivery_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `precio` decimal(8,2) NOT NULL,
  `menu_id` bigint NOT NULL,
  `descripcion` longtext,
  PRIMARY KEY (`id`),
  KEY `delivery_producto_menu_id_aecf43ed_fk_delivery_menu_id` (`menu_id`),
  CONSTRAINT `delivery_producto_menu_id_aecf43ed_fk_delivery_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `delivery_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_producto`
--

LOCK TABLES `delivery_producto` WRITE;
/*!40000 ALTER TABLE `delivery_producto` DISABLE KEYS */;
INSERT INTO `delivery_producto` VALUES (1,'Libreta',12.00,1,'fefwfwfa');
/*!40000 ALTER TABLE `delivery_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_rating`
--

DROP TABLE IF EXISTS `delivery_rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_rating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` int NOT NULL,
  `empleado_id` bigint DEFAULT NULL,
  `comentario` longtext,
  PRIMARY KEY (`id`),
  KEY `delivery_rating_empleado_id_b066e9f7` (`empleado_id`),
  CONSTRAINT `delivery_rating_empleado_id_b066e9f7_fk_delivery_employee_id` FOREIGN KEY (`empleado_id`) REFERENCES `delivery_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_rating`
--

LOCK TABLES `delivery_rating` WRITE;
/*!40000 ALTER TABLE `delivery_rating` DISABLE KEYS */;
/*!40000 ALTER TABLE `delivery_rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_restaurante`
--

DROP TABLE IF EXISTS `delivery_restaurante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_restaurante` (
  `cliente_ptr_id` bigint NOT NULL,
  `NRC` varchar(15) NOT NULL,
  `Empleados` int NOT NULL,
  `Propietario` varchar(40) NOT NULL,
  PRIMARY KEY (`cliente_ptr_id`),
  UNIQUE KEY `delivery_restaurante_NRC_3c5e4972_uniq` (`NRC`),
  CONSTRAINT `delivery_restaurante_cliente_ptr_id_441aee73_fk_delivery_` FOREIGN KEY (`cliente_ptr_id`) REFERENCES `delivery_cliente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_restaurante`
--

LOCK TABLES `delivery_restaurante` WRITE;
/*!40000 ALTER TABLE `delivery_restaurante` DISABLE KEYS */;
INSERT INTO `delivery_restaurante` VALUES (1,'21312312312323',3,'Abel Ríos González');
/*!40000 ALTER TABLE `delivery_restaurante` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `evitar_duplicados_nrc` BEFORE INSERT ON `delivery_restaurante` FOR EACH ROW BEGIN
    IF EXISTS (SELECT 1 FROM delivery_restaurante WHERE NRC = NEW.NRC) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ya existe un restaurante con este NRC';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `delivery_usuario`
--

DROP TABLE IF EXISTS `delivery_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_usuario` (
  `cliente_ptr_id` bigint NOT NULL,
  `DNI` varchar(9) NOT NULL,
  `Apellidos` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cliente_ptr_id`),
  UNIQUE KEY `delivery_usuario_DNI_09733bd0_uniq` (`DNI`),
  CONSTRAINT `delivery_usuario_cliente_ptr_id_5c2d3077_fk_delivery_cliente_id` FOREIGN KEY (`cliente_ptr_id`) REFERENCES `delivery_cliente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_usuario`
--

LOCK TABLES `delivery_usuario` WRITE;
/*!40000 ALTER TABLE `delivery_usuario` DISABLE KEYS */;
INSERT INTO `delivery_usuario` VALUES (2,'77644571K','Illán'),(3,'21231231W','Méndez Álvarez'),(4,'54343545A','Pérez Valero');
/*!40000 ALTER TABLE `delivery_usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `evitar_duplicados_dni` BEFORE INSERT ON `delivery_usuario` FOR EACH ROW BEGIN
    IF EXISTS (SELECT 1 FROM delivery_usuario WHERE DNI = NEW.DNI) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ya existe un usuario con este DNI';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `delivery_worktime`
--

DROP TABLE IF EXISTS `delivery_worktime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_worktime` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `efficiency` int NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) NOT NULL,
  `employee_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `delivery_worktime_employee_id_2147c96a_fk_delivery_employee_id` (`employee_id`),
  CONSTRAINT `delivery_worktime_employee_id_2147c96a_fk_delivery_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `delivery_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_worktime`
--

LOCK TABLES `delivery_worktime` WRITE;
/*!40000 ALTER TABLE `delivery_worktime` DISABLE KEYS */;
/*!40000 ALTER TABLE `delivery_worktime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-01-14 13:57:33.185659','1','Restaurante Bar Paco - 1',1,'[{\"added\": {}}]',9,1),(2,'2024-01-14 16:05:51.338818','1','Menu Bar Paco',1,'[{\"added\": {}}, {\"added\": {\"name\": \"producto\", \"object\": \"Libreta - $12\"}}]',16,1),(3,'2024-01-14 16:06:26.025749','1','Pedido 1 - Estado: preparacion',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detalle pedido\", \"object\": \"DetallePedido object (1)\"}}]',7,1),(4,'2024-01-14 16:18:39.211232','1','Mario - ID:1',1,'[{\"added\": {}}]',11,1),(5,'2024-01-14 16:19:28.971118','2','Pedido 2 - Estado: preparacion',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detalle pedido\", \"object\": \"DetallePedido object (2)\"}}]',7,1),(6,'2024-01-15 11:15:47.463714','1','Pedido 1 - Estado: En preparación',3,'',7,1),(7,'2024-01-15 11:17:42.190870','4','Pedido 4 - Estado: preparacion',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detalle pedido\", \"object\": \"DetallePedido object (3)\"}}]',7,1),(8,'2024-01-15 11:29:58.554589','4','Pedido 4 - Estado: preparacion',3,'',7,1),(9,'2024-01-15 11:30:07.654396','5','Pedido 5 - Estado: preparacion',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detalle pedido\", \"object\": \"DetallePedido object (4)\"}}]',7,1),(10,'2024-01-15 11:31:26.457909','5','Pedido 5 - Estado: preparacion',3,'',7,1),(11,'2024-01-15 11:31:34.095341','6','Pedido 6 - Estado: En Preparacion',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detalle pedido\", \"object\": \"DetallePedido object (5)\"}}]',7,1),(12,'2024-01-15 11:45:06.694258','6','Pedido 6 - Estado: En Preparacion',3,'',7,1),(13,'2024-01-15 11:45:14.620480','7','Pedido 7 - Estado: En Preparación',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detalle pedido\", \"object\": \"DetallePedido object (6)\"}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(19,'delivery','asigna'),(8,'delivery','cliente'),(18,'delivery','detallepedido'),(11,'delivery','employee'),(20,'delivery','encarga'),(14,'delivery','gasto'),(15,'delivery','ingreso'),(16,'delivery','menu'),(7,'delivery','pedido'),(17,'delivery','producto'),(12,'delivery','rating'),(9,'delivery','restaurante'),(10,'delivery','usuario'),(13,'delivery','worktime'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-01-14 13:45:05.441397'),(2,'auth','0001_initial','2024-01-14 13:45:07.332281'),(3,'admin','0001_initial','2024-01-14 13:45:07.830934'),(4,'admin','0002_logentry_remove_auto_add','2024-01-14 13:45:07.861745'),(5,'admin','0003_logentry_add_action_flag_choices','2024-01-14 13:45:07.897669'),(6,'contenttypes','0002_remove_content_type_name','2024-01-14 13:45:08.183024'),(7,'auth','0002_alter_permission_name_max_length','2024-01-14 13:45:08.393379'),(8,'auth','0003_alter_user_email_max_length','2024-01-14 13:45:08.515111'),(9,'auth','0004_alter_user_username_opts','2024-01-14 13:45:08.544919'),(10,'auth','0005_alter_user_last_login_null','2024-01-14 13:45:08.759409'),(11,'auth','0006_require_contenttypes_0002','2024-01-14 13:45:08.771373'),(12,'auth','0007_alter_validators_add_error_messages','2024-01-14 13:45:08.805223'),(13,'auth','0008_alter_user_username_max_length','2024-01-14 13:45:09.022758'),(14,'auth','0009_alter_user_last_name_max_length','2024-01-14 13:45:09.240258'),(15,'auth','0010_alter_group_name_max_length','2024-01-14 13:45:09.322962'),(16,'auth','0011_update_proxy_permissions','2024-01-14 13:45:09.359738'),(17,'auth','0012_alter_user_first_name_max_length','2024-01-14 13:45:09.593116'),(18,'delivery','0001_initial','2024-01-14 13:45:09.682874'),(19,'delivery','0002_delete_pedido','2024-01-14 13:45:09.740722'),(20,'delivery','0003_initial','2024-01-14 13:45:09.833472'),(21,'delivery','0004_alter_pedido_precio','2024-01-14 13:45:10.134853'),(22,'delivery','0005_encarga','2024-01-14 13:45:10.403090'),(23,'delivery','0006_alter_encarga_pedido','2024-01-14 13:45:10.781936'),(24,'delivery','0007_remove_pedido_codigopedido','2024-01-14 13:45:10.860727'),(25,'delivery','0008_producto','2024-01-14 13:45:10.939632'),(26,'delivery','0009_cliente_remove_pedido_cantidad_and_more','2024-01-14 13:45:12.902441'),(27,'delivery','0010_employee_rating_worktime','2024-01-14 13:45:13.349180'),(28,'delivery','0011_remove_pedido_productos_pedido_cantidad_and_more','2024-01-14 13:45:14.112031'),(29,'delivery','0012_gasto_ingreso_rating_empleado_worktime_empleado_and_more','2024-01-14 13:45:18.442459'),(30,'delivery','0013_employee_telefono','2024-01-14 13:45:18.585072'),(31,'delivery','0014_remove_emite_empleado_emite_pedido','2024-01-14 13:45:19.015054'),(32,'delivery','0015_remove_gasto_destinatario_remove_ingreso_emisor','2024-01-14 13:45:19.164523'),(33,'delivery','0016_remove_worktime_empleado_schedule','2024-01-14 13:45:19.654213'),(34,'delivery','0017_schedule_worktime','2024-01-14 13:45:19.880607'),(35,'delivery','0018_remove_rating_empleado_generate','2024-01-14 13:45:20.219701'),(36,'delivery','0019_alter_generate_rating','2024-01-14 13:45:20.751500'),(37,'delivery','0020_alter_rating_rating','2024-01-14 13:45:20.908866'),(38,'delivery','0021_menu_producto_rating_empleado_alter_employee_nombre_and_more','2024-01-14 13:45:22.022887'),(39,'delivery','0022_remove_pedido_cantidad_remove_pedido_nombre_producto_and_more','2024-01-14 13:45:22.855654'),(40,'delivery','0023_alter_restaurante_propietario','2024-01-14 13:45:22.931456'),(41,'delivery','0024_remove_menu_restaurante_menu_nombre_restaurante_menu','2024-01-14 13:45:23.434107'),(42,'delivery','0025_pedido_latitud_pedido_longitud','2024-01-14 13:45:23.643836'),(43,'delivery','0026_auto_20231224_1225','2024-01-14 13:45:23.658507'),(44,'delivery','0027_pedido_restaurante','2024-01-14 13:45:23.970676'),(45,'delivery','0028_alter_pedido_restaurante','2024-01-14 13:45:24.196207'),(46,'delivery','0029_remove_pedido_restaurante','2024-01-14 13:45:24.476500'),(47,'delivery','0030_remove_pedido_productos','2024-01-14 13:45:24.534166'),(48,'delivery','0031_pedido_productos_pedido_restaurante','2024-01-14 13:45:24.859297'),(49,'delivery','0032_alter_detallepedido_cantidad','2024-01-14 13:45:24.905180'),(50,'delivery','0033_alter_detallepedido_cantidad','2024-01-14 13:45:24.957080'),(51,'delivery','0034_alter_detallepedido_cantidad','2024-01-14 13:45:25.014882'),(52,'delivery','0035_alter_detallepedido_unique_together','2024-01-14 13:45:25.100762'),(53,'delivery','0036_alter_detallepedido_unique_together','2024-01-14 13:45:25.338019'),(54,'delivery','0037_alter_detallepedido_unique_together','2024-01-14 13:45:25.424785'),(55,'delivery','0038_delete_comunica','2024-01-14 13:45:25.493605'),(56,'delivery','0039_rename_estado_pedido_estado_pedido_fecha_creacion','2024-01-14 13:45:25.769059'),(57,'delivery','0040_remove_menu_nombre_remove_restaurante_menu_and_more','2024-01-14 13:45:27.268854'),(58,'delivery','0041_alter_pedido_productos','2024-01-14 13:45:27.317725'),(59,'delivery','0042_remove_menu_productos','2024-01-14 13:45:27.432549'),(60,'delivery','0043_menu_productos','2024-01-14 13:45:27.980954'),(61,'delivery','0044_remove_pedido_precio_total','2024-01-14 13:45:28.116706'),(62,'delivery','0045_ingreso_pedido_delete_emite','2024-01-14 13:45:28.381879'),(63,'delivery','0046_alter_gasto_importe_alter_ingreso_importe','2024-01-14 13:45:28.729950'),(64,'delivery','0047_usuario_apellidos','2024-01-14 13:45:28.828757'),(65,'delivery','0048_remove_encarga_pedido_remove_encarga_usuario_and_more','2024-01-14 13:45:32.709364'),(66,'delivery','0049_remove_pedido_empleado_asignado_alter_usuario_dni_and_more','2024-01-14 13:45:33.710668'),(67,'delivery','0050_remove_employee_gasto_remove_pedido_gasto_generado_and_more','2024-01-14 13:45:35.443038'),(68,'sessions','0001_initial','2024-01-14 13:45:35.567669'),(69,'delivery','0051_employee_disponible_alter_usuario_pedidos','2024-01-14 14:37:59.118332'),(70,'delivery','0052_pedido_repartidor','2024-01-14 15:06:07.221439'),(71,'delivery','0053_remove_usuario_pedidos_encarga','2024-01-15 10:52:08.717214'),(72,'delivery','0054_pedido_usuario','2024-01-15 11:05:32.821946'),(73,'delivery','0055_remove_pedido_latitud_remove_pedido_longitud','2024-01-15 11:17:33.627583'),(74,'delivery','0056_alter_pedido_estado','2024-01-15 11:20:25.190414'),(75,'delivery','0057_alter_pedido_estado','2024-01-15 11:31:15.845245'),(76,'delivery','0058_alter_pedido_estado','2024-01-15 13:16:22.785048');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('a0b2yceofavx5zrdmvocalnsl0thc4rt','.eJxVjEEOgjAQRe_StWlmWrDUpXvO0Mx0OoIaSCisjHdXEha6_e-9_zKJtnVIWy1LGsVcDJrT78aUH2Xagdxpus02z9O6jGx3xR602n6W8rwe7t_BQHX41kDECC7EKArM6mOHJC0Tej6L14hZAbRpVYLDBiRL9AG1EwF2xZn3B_g2OHY:1rP0yM:rR9Hz1NMCR4Yb2ePU7Dv881ASTtACErBvOf1vg_-bBk','2024-01-28 13:56:22.474585');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'deliverydb'
--
/*!50106 SET @save_time_zone= @@TIME_ZONE */ ;
/*!50106 DROP EVENT IF EXISTS `cambiar_estado_pedido_evento` */;
DELIMITER ;;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;;
/*!50003 SET character_set_client  = utf8mb4 */ ;;
/*!50003 SET character_set_results = utf8mb4 */ ;;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;;
/*!50003 SET @saved_time_zone      = @@time_zone */ ;;
/*!50003 SET time_zone             = 'SYSTEM' */ ;;
/*!50106 CREATE*/ /*!50117 DEFINER=`root`@`localhost`*/ /*!50106 EVENT `cambiar_estado_pedido_evento` ON SCHEDULE EVERY 1 MINUTE STARTS '2024-01-15 02:34:17' ON COMPLETION NOT PRESERVE ENABLE DO BEGIN
    -- Actualizar estado de los pedidos de 'En Preparación' a 'En Envío' después de 1 minuto
    UPDATE delivery_pedido
    SET estado = 'En Envío'
    WHERE estado = 'En Preparación' AND TIMESTAMPDIFF(MINUTE, created_at, NOW()) >= 1;

    -- Actualizar estado de los pedidos de 'En Envío' a 'Entregado' después de 1 minuto
    UPDATE delivery_pedido
    SET estado = 'Entregado'
    WHERE estado = 'En Envío' AND TIMESTAMPDIFF(MINUTE, created_at, NOW()) >= 1 AND estado != 'Entregado';
END */ ;;
/*!50003 SET time_zone             = @saved_time_zone */ ;;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;;
/*!50003 SET character_set_client  = @saved_cs_client */ ;;
/*!50003 SET character_set_results = @saved_cs_results */ ;;
/*!50003 SET collation_connection  = @saved_col_connection */ ;;
DELIMITER ;
/*!50106 SET TIME_ZONE= @save_time_zone */ ;

--
-- Dumping routines for database 'deliverydb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-15 18:42:36
