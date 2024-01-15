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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-15 18:33:35
