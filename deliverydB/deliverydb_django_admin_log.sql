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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-15 18:33:28
