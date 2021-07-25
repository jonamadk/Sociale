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
INSERT INTO `auth_group` VALUES (1,'bank staff');
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (2,1,14),(4,1,27),(1,1,31),(3,1,35);
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
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add user',4,'add_usermodel'),(14,'Can change user',4,'change_usermodel'),(15,'Can delete user',4,'delete_usermodel'),(16,'Can view user',4,'view_usermodel'),(17,'Can add template resource',5,'add_templateresource'),(18,'Can change template resource',5,'change_templateresource'),(19,'Can delete template resource',5,'delete_templateresource'),(20,'Can view template resource',5,'view_templateresource'),(21,'Can add mf hash',6,'add_mfhash'),(22,'Can change mf hash',6,'change_mfhash'),(23,'Can delete mf hash',6,'delete_mfhash'),(24,'Can view mf hash',6,'view_mfhash'),(25,'Can add target user group',7,'add_targetusergroup'),(26,'Can change target user group',7,'change_targetusergroup'),(27,'Can delete target user group',7,'delete_targetusergroup'),(28,'Can view target user group',7,'view_targetusergroup'),(29,'Can add campaign',8,'add_campaign'),(30,'Can change campaign',8,'change_campaign'),(31,'Can delete campaign',8,'delete_campaign'),(32,'Can view campaign',8,'view_campaign'),(33,'Can add target user',9,'add_targetuser'),(34,'Can change target user',9,'change_targetuser'),(35,'Can delete target user',9,'delete_targetuser'),(36,'Can view target user',9,'view_targetuser'),(37,'Can add target user csv',10,'add_targetusercsv'),(38,'Can change target user csv',10,'change_targetusercsv'),(39,'Can delete target user csv',10,'delete_targetusercsv'),(40,'Can view target user csv',10,'view_targetusercsv'),(41,'Can add log entry',11,'add_logentry'),(42,'Can change log entry',11,'change_logentry'),(43,'Can delete log entry',11,'delete_logentry'),(44,'Can view log entry',11,'view_logentry'),(45,'Can add session',12,'add_session'),(46,'Can change session',12,'change_session'),(47,'Can delete session',12,'delete_session'),(48,'Can view session',12,'view_session'),(49,'Can add Token',13,'add_token'),(50,'Can change Token',13,'change_token'),(51,'Can delete Token',13,'delete_token'),(52,'Can view Token',13,'view_token'),(53,'Can add token',14,'add_tokenproxy'),(54,'Can change token',14,'change_tokenproxy'),(55,'Can delete token',14,'delete_tokenproxy'),(56,'Can view token',14,'view_tokenproxy'),(57,'Can add exploit data',15,'add_exploitdata'),(58,'Can change exploit data',15,'change_exploitdata'),(59,'Can delete exploit data',15,'delete_exploitdata'),(60,'Can view exploit data',15,'view_exploitdata');
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
INSERT INTO `authtoken_token` VALUES ('3254ef77a35c5eda74b91cedb73fe4a233051255','2021-07-04 11:31:53.093728',1),('6b23345e5b83180fdcb9a060db8231a7f33d8569','2021-07-04 11:35:00.946871',2);
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
  `templateresource_id` int NOT NULL,
  `start_date` varchar(250) DEFAULT NULL,
  `end_date` varchar(240) DEFAULT NULL,
  `user_id` int NOT NULL,
  `target_users_mail_list` longtext,
  `campaign_opened_count` int NOT NULL,
  `hide_camapaign_status` tinyint(1) NOT NULL,
  `campaign_schedule_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
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
  PRIMARY KEY (`id`)
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
  `status` tinyint(1) NOT NULL,
  `email_credential` varchar(254) DEFAULT NULL,
  `password_credential` varchar(254) DEFAULT NULL,
  `leaked_password_credential` varchar(254) DEFAULT NULL,
  `user_agent_data` longtext,
  `more_details` longtext,
  `all_data` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
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
  PRIMARY KEY (`id`)
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
  PRIMARY KEY (`id`)
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
  PRIMARY KEY (`id`)
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
INSERT INTO `django_admin_log` VALUES (1,'2021-07-04 11:31:53.096281','1','3254ef77a35c5eda74b91cedb73fe4a233051255',1,'[{\"added\": {}}]',14,1),(2,'2021-07-04 11:35:16.901105','2','socialetest',2,'[{\"changed\": {\"fields\": [\"Superuser status\", \"Staff status\"]}}]',4,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (11,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(13,'authtoken','token'),(14,'authtoken','tokenproxy'),(8,'campaign','campaign'),(9,'campaign','targetuser'),(10,'campaign','targetusercsv'),(7,'campaign','targetusergroup'),(3,'contenttypes','contenttype'),(15,'exploit_data','exploitdata'),(6,'qrotp','mfhash'),(12,'sessions','session'),(5,'template','templateresource'),(4,'user','usermodel');
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
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-07-04 11:30:33.646026'),(2,'contenttypes','0002_remove_content_type_name','2021-07-04 11:30:33.834669'),(3,'auth','0001_initial','2021-07-04 11:30:34.066322'),(4,'auth','0002_alter_permission_name_max_length','2021-07-04 11:30:34.531350'),(5,'auth','0003_alter_user_email_max_length','2021-07-04 11:30:34.562183'),(6,'auth','0004_alter_user_username_opts','2021-07-04 11:30:34.577442'),(7,'auth','0005_alter_user_last_login_null','2021-07-04 11:30:34.586550'),(8,'auth','0006_require_contenttypes_0002','2021-07-04 11:30:34.592287'),(9,'auth','0007_alter_validators_add_error_messages','2021-07-04 11:30:34.621392'),(10,'auth','0008_alter_user_username_max_length','2021-07-04 11:30:34.647780'),(11,'auth','0009_alter_user_last_name_max_length','2021-07-04 11:30:34.659795'),(12,'auth','0010_alter_group_name_max_length','2021-07-04 11:30:34.687020'),(13,'auth','0011_update_proxy_permissions','2021-07-04 11:30:34.719812'),(14,'auth','0012_alter_user_first_name_max_length','2021-07-04 11:30:34.732371'),(15,'admin','0001_initial','2021-07-04 11:30:39.868118'),(16,'admin','0002_logentry_remove_auto_add','2021-07-04 11:30:40.156973'),(17,'admin','0003_logentry_add_action_flag_choices','2021-07-04 11:30:40.171374'),(18,'authtoken','0001_initial','2021-07-04 11:30:40.245178'),(19,'authtoken','0002_auto_20160226_1747','2021-07-04 11:30:40.498541'),(20,'authtoken','0003_tokenproxy','2021-07-04 11:30:40.515778'),(21,'exploit_data','0001_initial','2021-07-04 11:30:40.581604'),(22,'exploit_data','0002_exploitdata_activated','2021-07-04 11:30:40.635715'),(23,'exploit_data','0003_auto_20210623_1058','2021-07-04 11:30:40.700580'),(24,'exploit_data','0004_auto_20210623_1103','2021-07-04 11:30:40.740628'),(25,'exploit_data','0005_exploitdata_browser_version','2021-07-04 11:30:40.795355'),(26,'sessions','0001_initial','2021-07-04 11:30:40.848857');
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
INSERT INTO `django_session` VALUES ('1dk43p9rz2lw4ofyxs3vp1e348fnkchj','.eJxVjDsOwyAQRO9CHSFYfiZlep8BLSwEJxGWjF1FuXtsyUVSjTTvzbxZwG2tYet5CROxK5Ps8ttFTM_cDkAPbPeZp7mtyxT5ofCTdj7OlF-30_07qNjrvhakCkjSmJyRPqvBGpLokwdwWg0YvYA9jLAKDdhcHBSRdC4JDAjn2ecLyRY3DQ:1m00Li:T06Uvmzx33vLZKFNmpiYYXY7odOcUbnFsoiB240OnLo','2021-07-18 11:31:46.851565'),('9ym0d824fahno79tppi7wuw3v2j6teuz','.eJxVjDsOwyAQRO9CHSFYfiZlep8BLSwEJxGWjF1FuXtsyUVSjTTvzbxZwG2tYet5CROxK5Ps8ttFTM_cDkAPbPeZp7mtyxT5ofCTdj7OlF-30_07qNjrvhakCkjSmJyRPqvBGpLokwdwWg0YvYA9jLAKDdhcHBSRdC4JDAjn2ecLyRY3DQ:1m00Me:BI_z4JUfIX076U9fgi1t7J74NrigvKm9J0y2CSI02XA','2021-07-18 11:32:44.177018');
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
  `browser_version` varchar(250) DEFAULT NULL,
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
  UNIQUE KEY `user_id` (`user_id`)
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
  UNIQUE KEY `template_name` (`template_name`)
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
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phonenumber` (`phonenumber`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_usermodel`
--

LOCK TABLES `user_usermodel` WRITE;
/*!40000 ALTER TABLE `user_usermodel` DISABLE KEYS */;
INSERT INTO `user_usermodel` VALUES (1,'pbkdf2_sha256$216000$xaTqFzP9CVOq$uMxVn+PNIoDaDu7vPqgOEBOhO64GzV6C0wfiRDdWRu8=','2021-07-04 11:32:44.172484',1,'sociale','','','nepbuzz5@gmail.com',1,1,'2021-07-04 11:31:24.873711','',NULL,0,0,0),(2,'pbkdf2_sha256$216000$BYTcL39W8LXG$wS3w0SzFYuo8mYBPfengM2GThAHB8OE+X3UIjFdzTR4=',NULL,1,'socialetest','Sociale','Test','adkmanoz38@gmail.com',1,1,'2021-07-04 11:35:00.000000','+9779843842514',NULL,0,0,0);
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
  PRIMARY KEY (`id`)
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

-- Dump completed on 2021-07-04 17:21:19
