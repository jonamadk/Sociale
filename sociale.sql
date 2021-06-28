-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: Sociale
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'group 1');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,4),(3,1,6);
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
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add user',4,'add_usermodel'),(14,'Can change user',4,'change_usermodel'),(15,'Can delete user',4,'delete_usermodel'),(16,'Can view user',4,'view_usermodel'),(17,'Can add template',5,'add_template'),(18,'Can change template',5,'change_template'),(19,'Can delete template',5,'delete_template'),(20,'Can view template',5,'view_template'),(21,'Can add template resource',6,'add_templateresource'),(22,'Can change template resource',6,'change_templateresource'),(23,'Can delete template resource',6,'delete_templateresource'),(24,'Can view template resource',6,'view_templateresource'),(25,'Can add mf hash',7,'add_mfhash'),(26,'Can change mf hash',7,'change_mfhash'),(27,'Can delete mf hash',7,'delete_mfhash'),(28,'Can view mf hash',7,'view_mfhash'),(29,'Can add log entry',8,'add_logentry'),(30,'Can change log entry',8,'change_logentry'),(31,'Can delete log entry',8,'delete_logentry'),(32,'Can view log entry',8,'view_logentry'),(33,'Can add session',9,'add_session'),(34,'Can change session',9,'change_session'),(35,'Can delete session',9,'delete_session'),(36,'Can view session',9,'view_session'),(37,'Can add Token',10,'add_token'),(38,'Can change Token',10,'change_token'),(39,'Can delete Token',10,'delete_token'),(40,'Can view Token',10,'view_token'),(41,'Can add token',11,'add_tokenproxy'),(42,'Can change token',11,'change_tokenproxy'),(43,'Can delete token',11,'delete_tokenproxy'),(44,'Can view token',11,'view_tokenproxy'),(45,'Can add exploit data',12,'add_exploitdata'),(46,'Can change exploit data',12,'change_exploitdata'),(47,'Can delete exploit data',12,'delete_exploitdata'),(48,'Can view exploit data',12,'view_exploitdata'),(49,'Can add target user',13,'add_targetuser'),(50,'Can change target user',13,'change_targetuser'),(51,'Can delete target user',13,'delete_targetuser'),(52,'Can view target user',13,'view_targetuser'),(53,'Can add campaign',14,'add_campaign'),(54,'Can change campaign',14,'change_campaign'),(55,'Can delete campaign',14,'delete_campaign'),(56,'Can view campaign',14,'view_campaign'),(57,'Can add target user group',15,'add_targetusergroup'),(58,'Can change target user group',15,'change_targetusergroup'),(59,'Can delete target user group',15,'delete_targetusergroup'),(60,'Can view target user group',15,'view_targetusergroup'),(61,'Can add target user csv',16,'add_targetusercsv'),(62,'Can change target user csv',16,'change_targetusercsv'),(63,'Can delete target user csv',16,'delete_targetusercsv'),(64,'Can view target user csv',16,'view_targetusercsv');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_user_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `user_usermodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('6540acb6dfb72fc9520b0b58137440b193daad8e','2021-06-25 05:04:09.070712',2),('a2fcb2605c589a22783dfe36d3d64d12eb8538bb','2021-06-25 05:00:36.054032',1);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campaign_campaign`
--

DROP TABLE IF EXISTS `campaign_campaign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campaign_campaign` (
  `id` int NOT NULL AUTO_INCREMENT,
  `campaign_name` varchar(254) DEFAULT NULL,
  `campaign_title` varchar(250) DEFAULT NULL,
  `start_date` varchar(250) DEFAULT NULL,
  `end_date` varchar(240) DEFAULT NULL,
  `user_id` int NOT NULL,
  `templateresource_id` int NOT NULL,
  `target_users_mail_list` longtext,
  `campaign_opened_count` int NOT NULL,
  `hide_camapaign_status` tinyint(1) NOT NULL,
  `campaign_schedule_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `campaign_campaign_user_id_ce558765_fk_user_usermodel_id` (`user_id`),
  KEY `campaign_campaign_templateresource_id_bbedc006` (`templateresource_id`),
  CONSTRAINT `campaign_campaign_templateresource_id_bbedc006_fk_template_` FOREIGN KEY (`templateresource_id`) REFERENCES `template_templateresource` (`id`),
  CONSTRAINT `campaign_campaign_user_id_ce558765_fk_user_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `user_usermodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign_campaign`
--

LOCK TABLES `campaign_campaign` WRITE;
/*!40000 ALTER TABLE `campaign_campaign` DISABLE KEYS */;
/*!40000 ALTER TABLE `campaign_campaign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campaign_campaign_targetusergroup`
--

DROP TABLE IF EXISTS `campaign_campaign_targetusergroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campaign_campaign_targetusergroup` (
  `id` int NOT NULL AUTO_INCREMENT,
  `campaign_id` int NOT NULL,
  `targetusergroup_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `campaign_campaign_target_campaign_id_targetusergr_7647cb88_uniq` (`campaign_id`,`targetusergroup_id`),
  KEY `campaign_campaign_ta_targetusergroup_id_f78a8b4c_fk_campaign_` (`targetusergroup_id`),
  CONSTRAINT `campaign_campaign_ta_campaign_id_129f8e2f_fk_campaign_` FOREIGN KEY (`campaign_id`) REFERENCES `campaign_campaign` (`id`),
  CONSTRAINT `campaign_campaign_ta_targetusergroup_id_f78a8b4c_fk_campaign_` FOREIGN KEY (`targetusergroup_id`) REFERENCES `campaign_targetusergroup` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign_campaign_targetusergroup`
--

LOCK TABLES `campaign_campaign_targetusergroup` WRITE;
/*!40000 ALTER TABLE `campaign_campaign_targetusergroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `campaign_campaign_targetusergroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campaign_targetuser`
--

DROP TABLE IF EXISTS `campaign_targetuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campaign_targetuser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `target_user_uuid` char(32) DEFAULT NULL,
  `email_credential` varchar(254) DEFAULT NULL,
  `password_credential` varchar(254) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `leaked_password_credential` varchar(254) DEFAULT NULL,
  `user_agent_data` longtext,
  `more_details` longtext,
  `all_data` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `campaign_targetuser_email_8cf9b264_uniq` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign_targetuser`
--

LOCK TABLES `campaign_targetuser` WRITE;
/*!40000 ALTER TABLE `campaign_targetuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `campaign_targetuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campaign_targetuser_opened_campaign_list`
--

DROP TABLE IF EXISTS `campaign_targetuser_opened_campaign_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campaign_targetuser_opened_campaign_list` (
  `id` int NOT NULL AUTO_INCREMENT,
  `targetuser_id` int NOT NULL,
  `campaign_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `campaign_targetuser_open_targetuser_id_campaign_i_63563dcc_uniq` (`targetuser_id`,`campaign_id`),
  KEY `campaign_targetuser__campaign_id_60f7e1a5_fk_campaign_` (`campaign_id`),
  CONSTRAINT `campaign_targetuser__campaign_id_60f7e1a5_fk_campaign_` FOREIGN KEY (`campaign_id`) REFERENCES `campaign_campaign` (`id`),
  CONSTRAINT `campaign_targetuser__targetuser_id_2597c984_fk_campaign_` FOREIGN KEY (`targetuser_id`) REFERENCES `campaign_targetuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign_targetuser_opened_campaign_list`
--

LOCK TABLES `campaign_targetuser_opened_campaign_list` WRITE;
/*!40000 ALTER TABLE `campaign_targetuser_opened_campaign_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `campaign_targetuser_opened_campaign_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campaign_targetuser_targetusergroup`
--

DROP TABLE IF EXISTS `campaign_targetuser_targetusergroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campaign_targetuser_targetusergroup` (
  `id` int NOT NULL AUTO_INCREMENT,
  `targetuser_id` int NOT NULL,
  `targetusergroup_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `campaign_targetuser_targ_targetuser_id_targetuser_ebe477f0_uniq` (`targetuser_id`,`targetusergroup_id`),
  KEY `campaign_targetuser__targetusergroup_id_4a6cb9a3_fk_campaign_` (`targetusergroup_id`),
  CONSTRAINT `campaign_targetuser__targetuser_id_233d71d8_fk_campaign_` FOREIGN KEY (`targetuser_id`) REFERENCES `campaign_targetuser` (`id`),
  CONSTRAINT `campaign_targetuser__targetusergroup_id_4a6cb9a3_fk_campaign_` FOREIGN KEY (`targetusergroup_id`) REFERENCES `campaign_targetusergroup` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign_targetuser_targetusergroup`
--

LOCK TABLES `campaign_targetuser_targetusergroup` WRITE;
/*!40000 ALTER TABLE `campaign_targetuser_targetusergroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `campaign_targetuser_targetusergroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campaign_targetusercsv`
--

DROP TABLE IF EXISTS `campaign_targetusercsv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campaign_targetusercsv` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file_name` varchar(100) NOT NULL,
  `uploaded` datetime(6) NOT NULL,
  `activated` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign_targetusercsv`
--

LOCK TABLES `campaign_targetusercsv` WRITE;
/*!40000 ALTER TABLE `campaign_targetusercsv` DISABLE KEYS */;
/*!40000 ALTER TABLE `campaign_targetusercsv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campaign_targetusergroup`
--

DROP TABLE IF EXISTS `campaign_targetusergroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campaign_targetusergroup` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_name` varchar(254) DEFAULT NULL,
  `department` varchar(254) DEFAULT NULL,
  `organization` varchar(254) DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `campaign_targetusergroup_user_id_6678b2cb_fk_user_usermodel_id` (`user_id`),
  CONSTRAINT `campaign_targetusergroup_user_id_6678b2cb_fk_user_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `user_usermodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign_targetusergroup`
--

LOCK TABLES `campaign_targetusergroup` WRITE;
/*!40000 ALTER TABLE `campaign_targetusergroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `campaign_targetusergroup` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk_user_usermodel_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `user_usermodel` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-06-25 05:00:36.057282','1','a2fcb2605c589a22783dfe36d3d64d12eb8538bb',1,'[{\"added\": {}}]',11,1),(2,'2021-06-25 05:05:21.856468','2','socialetest',2,'[{\"changed\": {\"fields\": [\"Superuser status\"]}}]',4,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(10,'authtoken','token'),(11,'authtoken','tokenproxy'),(14,'campaign','campaign'),(13,'campaign','targetuser'),(16,'campaign','targetusercsv'),(15,'campaign','targetusergroup'),(3,'contenttypes','contenttype'),(12,'exploit_data','exploitdata'),(7,'qrotp','mfhash'),(9,'sessions','session'),(5,'template','template'),(6,'template','templateresource'),(4,'user','usermodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-06-25 04:56:21.895874'),(2,'contenttypes','0002_remove_content_type_name','2021-06-25 04:56:22.058116'),(3,'auth','0001_initial','2021-06-25 04:56:22.216704'),(4,'auth','0002_alter_permission_name_max_length','2021-06-25 04:56:22.744914'),(5,'auth','0003_alter_user_email_max_length','2021-06-25 04:56:22.762336'),(6,'auth','0004_alter_user_username_opts','2021-06-25 04:56:22.779209'),(7,'auth','0005_alter_user_last_login_null','2021-06-25 04:56:22.793262'),(8,'auth','0006_require_contenttypes_0002','2021-06-25 04:56:22.800546'),(9,'auth','0007_alter_validators_add_error_messages','2021-06-25 04:56:22.823107'),(10,'auth','0008_alter_user_username_max_length','2021-06-25 04:56:22.834676'),(11,'auth','0009_alter_user_last_name_max_length','2021-06-25 04:56:22.844360'),(12,'auth','0010_alter_group_name_max_length','2021-06-25 04:56:22.867942'),(13,'auth','0011_update_proxy_permissions','2021-06-25 04:56:22.880684'),(14,'auth','0012_alter_user_first_name_max_length','2021-06-25 04:56:22.889017'),(15,'admin','0001_initial','2021-06-25 04:56:33.737644'),(16,'admin','0002_logentry_remove_auto_add','2021-06-25 04:56:33.980368'),(17,'admin','0003_logentry_add_action_flag_choices','2021-06-25 04:56:33.993261'),(18,'authtoken','0001_initial','2021-06-25 04:56:34.058049'),(19,'authtoken','0002_auto_20160226_1747','2021-06-25 04:56:34.273944'),(20,'authtoken','0003_tokenproxy','2021-06-25 04:56:34.291144'),(21,'campaign','0001_initial','2021-06-25 04:56:34.422717'),(22,'campaign','0002_campaign_targetuser','2021-06-25 04:56:34.794954'),(23,'campaign','0003_auto_20210423_0651','2021-06-25 04:56:34.979735'),(24,'campaign','0004_auto_20210423_0842','2021-06-25 04:56:35.029478'),(25,'campaign','0005_auto_20210423_0843','2021-06-25 04:56:35.091877'),(26,'campaign','0006_auto_20210423_0902','2021-06-25 04:56:35.303912'),(27,'campaign','0007_auto_20210423_0932','2021-06-25 04:56:35.536963'),(28,'campaign','0008_auto_20210425_1006','2021-06-25 04:56:36.001289'),(29,'campaign','0009_targetuser_user','2021-06-25 04:56:36.103910'),(30,'campaign','0010_auto_20210427_0344','2021-06-25 04:56:36.153316'),(31,'campaign','0011_auto_20210427_0350','2021-06-25 04:56:36.299515'),(32,'campaign','0012_auto_20210427_0355','2021-06-25 04:56:36.340925'),(33,'campaign','0013_auto_20210427_0357','2021-06-25 04:56:36.428601'),(34,'campaign','0014_auto_20210430_0728','2021-06-25 04:56:36.704189'),(35,'campaign','0015_remove_targetuser_username','2021-06-25 04:56:36.784833'),(36,'campaign','0016_auto_20210505_0634','2021-06-25 04:56:37.129036'),(37,'campaign','0017_auto_20210505_1144','2021-06-25 04:56:37.620546'),(38,'campaign','0018_auto_20210505_1146','2021-06-25 04:56:37.649488'),(39,'campaign','0019_auto_20210505_1153','2021-06-25 04:56:37.829315'),(40,'campaign','0020_auto_20210506_0521','2021-06-25 04:56:37.841533'),(41,'campaign','0021_targetusercsv','2021-06-25 04:56:37.916122'),(42,'campaign','0022_auto_20210509_1018','2021-06-25 04:56:38.056711'),(43,'campaign','0023_auto_20210509_1103','2021-06-25 04:56:38.521984'),(44,'campaign','0024_auto_20210509_1150','2021-06-25 04:56:38.643019'),(45,'campaign','0025_auto_20210509_1200','2021-06-25 04:56:38.763975'),(46,'campaign','0026_campaign_target_users_mail_list','2021-06-25 04:56:38.914319'),(47,'campaign','0027_auto_20210521_1507','2021-06-25 04:56:39.130700'),(48,'campaign','0028_auto_20210527_0415','2021-06-25 04:56:39.248200'),(49,'campaign','0029_auto_20210527_1057','2021-06-25 04:56:39.479765'),(50,'campaign','0030_auto_20210527_1552','2021-06-25 04:56:39.902926'),(51,'campaign','0031_auto_20210527_1554','2021-06-25 04:56:39.952103'),(52,'campaign','0032_auto_20210527_1610','2021-06-25 04:56:39.990801'),(53,'campaign','0033_auto_20210528_0223','2021-06-25 04:56:40.148402'),(54,'campaign','0034_auto_20210528_0240','2021-06-25 04:56:40.516961'),(55,'campaign','0035_targetuser_opened_campaign_list','2021-06-25 04:56:40.786954'),(56,'campaign','0036_auto_20210601_0943','2021-06-25 04:56:42.091174'),(57,'campaign','0037_auto_20210601_0947','2021-06-25 04:56:42.250595'),(58,'campaign','0038_auto_20210601_0952','2021-06-25 04:56:42.462864'),(59,'campaign','0039_auto_20210601_1002','2021-06-25 04:56:42.619022'),(60,'campaign','0040_auto_20210601_1026','2021-06-25 04:56:42.668923'),(61,'campaign','0041_auto_20210601_1031','2021-06-25 04:56:42.713015'),(62,'campaign','0042_auto_20210601_1046','2021-06-25 04:56:42.729975'),(63,'campaign','0043_auto_20210602_0209','2021-06-25 04:56:42.902463'),(64,'campaign','0044_auto_20210602_0222','2021-06-25 04:56:43.101061'),(65,'campaign','0045_campaign_campaign_opened_count','2021-06-25 04:56:43.215710'),(66,'campaign','0046_auto_20210602_0236','2021-06-25 04:56:43.240219'),(67,'campaign','0047_targetuser_leaked_password_credential','2021-06-25 04:56:43.294665'),(68,'campaign','0048_campaign_hide_camapaign_status','2021-06-25 04:56:43.349597'),(69,'campaign','0049_auto_20210606_0858','2021-06-25 04:56:43.571601'),(70,'campaign','0050_campaign_campaign_schedule_status','2021-06-25 04:56:43.656991'),(71,'campaign','0051_auto_20210615_0831','2021-06-25 04:56:43.794683'),(72,'campaign','0052_targetuser_user_agent_data','2021-06-25 04:56:43.851851'),(73,'campaign','0053_auto_20210623_0752','2021-06-25 04:56:43.941987'),(74,'campaign','0054_auto_20210623_0901','2021-06-25 04:56:43.992207'),(75,'campaign','0055_remove_targetuser_all_data','2021-06-25 04:56:44.090336'),(76,'campaign','0056_targetuser_all_data','2021-06-25 04:56:44.156383'),(77,'exploit_data','0001_initial','2021-06-25 04:56:44.205035'),(78,'exploit_data','0002_exploitdata_activated','2021-06-25 04:56:44.250045'),(79,'exploit_data','0003_auto_20210623_1058','2021-06-25 04:56:44.325466'),(80,'exploit_data','0004_auto_20210623_1103','2021-06-25 04:56:44.355478'),(81,'sessions','0001_initial','2021-06-25 04:56:44.401210');
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
INSERT INTO `django_session` VALUES ('69su87jaof4ielskj1metwle7m6dgs9i','.eJxVjDEOwjAMRe-SGUV1ogabkZ0zRLaTkgJKpaadEHenlTrA-t77_20ir0uJa8tzHJO5GDCnXyasz1x3kR5c75PVqS7zKHZP7GGbvU0pv65H-3dQuJVtjd7DGQcVIgZ0KYiq61gJUNCnXgSBKTO7gX3oEIik37CCd-w4mM8X6fY4JA:1lwdx4:0VrfAGwj4OfTo-sn5yYN-h9ZKhLhTrGjih9X1IPS1Zw','2021-07-09 05:00:26.824640'),('y96814kz9acgiiszj97vh4a5yirexmnr','.eJxVjDEOwjAMRe-SGUV1ogabkZ0zRLaTkgJKpaadEHenlTrA-t77_20ir0uJa8tzHJO5GDCnXyasz1x3kR5c75PVqS7zKHZP7GGbvU0pv65H-3dQuJVtjd7DGQcVIgZ0KYiq61gJUNCnXgSBKTO7gX3oEIik37CCd-w4mM8X6fY4JA:1lwdv8:NwpGDOXLF9nLZuOTzFJm7gvBztPM7MQ4jwFwyBA9N0Y','2021-07-09 04:58:26.197114');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exploit_data_exploitdata`
--

DROP TABLE IF EXISTS `exploit_data_exploitdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exploit_data_exploitdata` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` longtext,
  `date` varchar(250) DEFAULT NULL,
  `author` varchar(250) DEFAULT NULL,
  `browser` varchar(250) DEFAULT NULL,
  `platform` varchar(250) DEFAULT NULL,
  `port` varchar(250) DEFAULT NULL,
  `activated` tinyint(1) NOT NULL,
  `type` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exploit_data_exploitdata`
--

LOCK TABLES `exploit_data_exploitdata` WRITE;
/*!40000 ALTER TABLE `exploit_data_exploitdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `exploit_data_exploitdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qrotp_mfhash`
--

DROP TABLE IF EXISTS `qrotp_mfhash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qrotp_mfhash` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mfa_hash` varchar(50) DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `qrotp_mfhash_user_id_45dbe29b_fk_user_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `user_usermodel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qrotp_mfhash`
--

LOCK TABLES `qrotp_mfhash` WRITE;
/*!40000 ALTER TABLE `qrotp_mfhash` DISABLE KEYS */;
INSERT INTO `qrotp_mfhash` VALUES (1,NULL,2);
/*!40000 ALTER TABLE `qrotp_mfhash` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `template_template`
--

DROP TABLE IF EXISTS `template_template`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `template_template` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `template_file` varchar(100) DEFAULT NULL,
  `created_date` varchar(50) DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `template_template_user_id_1bd8f26a_fk_user_usermodel_id` (`user_id`),
  CONSTRAINT `template_template_user_id_1bd8f26a_fk_user_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `user_usermodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `template_template`
--

LOCK TABLES `template_template` WRITE;
/*!40000 ALTER TABLE `template_template` DISABLE KEYS */;
/*!40000 ALTER TABLE `template_template` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `template_templateresource`
--

DROP TABLE IF EXISTS `template_templateresource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `template_templateresource` (
  `id` int NOT NULL AUTO_INCREMENT,
  `headerBackgroundColor` varchar(100) DEFAULT NULL,
  `headerFontColor` varchar(100) DEFAULT NULL,
  `headerNav1` varchar(100) DEFAULT NULL,
  `headerNav2` varchar(100) DEFAULT NULL,
  `headerNav3` varchar(100) DEFAULT NULL,
  `bodyBackgroundcolor` varchar(100) DEFAULT NULL,
  `bodyFontColor` varchar(100) DEFAULT NULL,
  `bodyButtonColor` varchar(120) DEFAULT NULL,
  `user_id` int NOT NULL,
  `template_name` varchar(250) DEFAULT NULL,
  `template_url` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `template_name` (`template_name`),
  KEY `template_templateresource_user_id_281c5945_fk_user_usermodel_id` (`user_id`),
  CONSTRAINT `template_templateresource_user_id_281c5945_fk_user_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `user_usermodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `template_templateresource`
--

LOCK TABLES `template_templateresource` WRITE;
/*!40000 ALTER TABLE `template_templateresource` DISABLE KEYS */;
/*!40000 ALTER TABLE `template_templateresource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_usermodel`
--

DROP TABLE IF EXISTS `user_usermodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_usermodel` (
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
  `phonenumber` varchar(128) NOT NULL,
  `otp_code` varchar(6) DEFAULT NULL,
  `email_two_factor_auth` tinyint(1) DEFAULT NULL,
  `totp_two_factor_auth` tinyint(1) DEFAULT NULL,
  `email_and_sms_two_factor_auth` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_usermodel`
--

LOCK TABLES `user_usermodel` WRITE;
/*!40000 ALTER TABLE `user_usermodel` DISABLE KEYS */;
INSERT INTO `user_usermodel` VALUES (1,'pbkdf2_sha256$216000$N7PaYrHKWNEe$xOvnj9DGRMpmqVh6tUvHaZ1oDZdnts4aouQzr8dZta4=','2021-06-25 05:00:26.815178',1,'sociale','','','nepbuzz5@gmail.com',1,1,'2021-06-25 04:57:41.430228','',NULL,0,0,0),(2,'pbkdf2_sha256$216000$jo9E0AacVPDt$YP6x+JTn4XQkS5pBwpNIoYj2IYSu/jSwKYEdFMPk9DA=',NULL,1,'socialetest','firstname','last_name','adkmanoz38@gmail.com',0,1,'2021-06-25 05:04:09.000000','+9779845270562',NULL,0,0,0);
/*!40000 ALTER TABLE `user_usermodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_usermodel_groups`
--

DROP TABLE IF EXISTS `user_usermodel_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_usermodel_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usermodel_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_usermodel_groups_usermodel_id_group_id_13d92115_uniq` (`usermodel_id`,`group_id`),
  KEY `user_usermodel_groups_group_id_85eb92aa_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_usermodel_groups_group_id_85eb92aa_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_usermodel_groups_usermodel_id_e061ce57_fk_user_usermodel_id` FOREIGN KEY (`usermodel_id`) REFERENCES `user_usermodel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_usermodel_groups`
--

LOCK TABLES `user_usermodel_groups` WRITE;
/*!40000 ALTER TABLE `user_usermodel_groups` DISABLE KEYS */;
INSERT INTO `user_usermodel_groups` VALUES (1,2,1);
/*!40000 ALTER TABLE `user_usermodel_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_usermodel_user_permissions`
--

DROP TABLE IF EXISTS `user_usermodel_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_usermodel_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usermodel_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_usermodel_user_perm_usermodel_id_permission__29df935f_uniq` (`usermodel_id`,`permission_id`),
  KEY `user_usermodel_user__permission_id_937fe129_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_usermodel_user__permission_id_937fe129_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_usermodel_user__usermodel_id_a6c3d649_fk_user_user` FOREIGN KEY (`usermodel_id`) REFERENCES `user_usermodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_usermodel_user_permissions`
--

LOCK TABLES `user_usermodel_user_permissions` WRITE;
/*!40000 ALTER TABLE `user_usermodel_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_usermodel_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-25 10:51:12
