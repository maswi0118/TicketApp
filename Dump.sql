-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: s403025
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `adminid` int NOT NULL AUTO_INCREMENT,
  `login` varchar(45) NOT NULL,
  `password` varchar(100) NOT NULL,
  `activated` tinyint DEFAULT '0',
  PRIMARY KEY (`adminid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'Piterek','15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225',1);
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artists`
--

DROP TABLE IF EXISTS `artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artists` (
  `aid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `genre` varchar(45) NOT NULL,
  `nationality` varchar(45) DEFAULT NULL,
  `about` varchar(45) DEFAULT NULL,
  `photolink` varchar(100) DEFAULT NULL,
  `artistscol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`aid`),
  UNIQUE KEY `ecid_UNIQUE` (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
INSERT INTO `artists` VALUES (1,'White 2115','Hip-Hop','Polska','White 2115, właściwie Sebastian Czekaj – pols','https://i.scdn.co/image/ab6761610000e5eb8c557a6da999d68fec818f79',NULL),(2,'Bedoes','Hip-Hop','Polska','Bedoes, właściwie Borys Przybylski – polski r','https://i.scdn.co/image/ab6761610000e5eba56ed11da36762cd6a91cf61',NULL),(3,'Tymek','Hip-Hop','Polska','Tymek lub Seven Phoenix, właściwie Tymoteusz ','https://i.scdn.co/image/ab6761610000e5eb87903a074cccd71d6bf110d8',NULL),(5,'Zabson','Hip-Hop','Polska','Żabson, właściwie Mateusz Zawistowski – polsk','https://i.scdn.co/image/ab6761610000e5eb3e6777761c6a709fa1276f2b',NULL),(6,'Malik Montana','Hip-Hop','Niemcy','Malik Montana, właściwie Mosa Ghawsi – niemie','https://i.scdn.co/image/ab6761610000e5ebde7885cffc35ab676e1191d7',NULL),(7,'Diho','Hip-Hop','Polska','Małpa','https://i.scdn.co/image/ab6761610000e5eb05dd414a3cc34a4440217596',NULL),(8,'Kizo','Hip-Hop','Polska','Kizo, właściwie Patryk Woziński – polski rape','https://i.scdn.co/image/ab6761610000e5eb6fb4daf897b5007df46669cc',NULL),(9,'The Weeknd','POP','Kanada','The Weeknd, właściwie Abel Makkonen Tesfaye –','https://i.scdn.co/image/ab6761610000e5eb2f71b65ef483ed75a8b40437',NULL),(10,'Kombii','Rock','Polska','Kombii – polski zespół grający muzykę z pogra','https://i.scdn.co/image/ab6761610000e5ebea580d44eaec603430b5dce8',NULL),(11,'Tommy Cash','Hip-Hop','Estonia','Tommy Cash, właściwie Tomas Tammemets – estoń','https://i.scdn.co/image/ab6761610000e5eb380e0710ccddd0fed1a569a6',NULL),(12,'Young Multi','Streamer','Polska','Mincrafter','https://i.scdn.co/image/ab6761610000e5ebf9e6a0935ffda86ce2e48840',NULL),(13,'Rogal DDL','Rap','Polska','Rogal DDL (wł. Marcin Rogala) – warszawski ra','https://i.scdn.co/image/ab67616d0000b27369dc949f2e643a73ad4042ee',NULL),(14,'Young Leosia','RAP','Polska','Young Leosia, dawniej Sara, właściwie Sara Le','https://i.scdn.co/image/ab6761610000e5eb10473747352aa2f233ce1870',NULL),(15,'Kwiat Jabloni','Folk','Polska','Kwiat Jabłoni – polski zespół muzyczny z Wars','https://i.scdn.co/image/ab6761610000e5ebc93f238813a2e0e7aefe84a2',NULL);
/*!40000 ALTER TABLE `artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `cid` int NOT NULL AUTO_INCREMENT,
  `city` varchar(45) NOT NULL,
  `province` varchar(45) NOT NULL,
  PRIMARY KEY (`cid`),
  UNIQUE KEY `city_UNIQUE` (`city`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES (1,'Kraków','Małopolskie'),(2,'Wrocław','Dolnośląskie'),(3,'Warszawa','Mazowieckie'),(4,'Poznań','Wielkopolskie'),(5,'Wieliczka','Małopolskie');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `eid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `date` datetime NOT NULL,
  `maxAmount` int NOT NULL DEFAULT '0',
  `sold` int NOT NULL DEFAULT '0',
  `lid` int NOT NULL,
  `income` double NOT NULL DEFAULT '0',
  `soldout` tinyint NOT NULL DEFAULT '0',
  `isOver` tinyint NOT NULL DEFAULT '0',
  `artists_aid` int NOT NULL,
  `price` double DEFAULT '0',
  PRIMARY KEY (`eid`,`artists_aid`),
  KEY `fk_events_locations1_idx` (`lid`),
  KEY `fk_events_artists1_idx` (`artists_aid`),
  CONSTRAINT `fk_events_artists1` FOREIGN KEY (`artists_aid`) REFERENCES `artists` (`aid`),
  CONSTRAINT `fk_events_locations1` FOREIGN KEY (`lid`) REFERENCES `locations` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3 KEY_BLOCK_SIZE=2;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,'Koncert White 2115','2022-03-04 19:00:00',2500,0,1,0,0,0,1,89),(3,'Koncert Kizo','2022-03-18 19:00:00',1500,0,2,0,0,0,8,59),(4,'The Weeknd W POLSCE!','2022-04-02 19:00:00',15000,0,3,0,0,0,9,289),(5,'Kombii gra w Wieliczce','2022-02-25 17:00:00',1500,0,9,0,0,0,10,29),(6,'Koncert White 2115','2022-02-19 19:00:00',1500,0,5,0,0,0,1,89),(7,'Koncert Bedoes','2022-02-26 19:00:00',1500,0,5,0,0,0,2,99),(8,'Koncert Kizo','2022-02-12 19:00:00',1500,0,5,0,0,0,8,99),(9,'Koncert Kizo','2022-02-19 19:30:00',45000,0,6,0,0,0,8,119),(10,'Koncert Diho','2022-02-12 19:30:00',4500,0,7,0,0,0,7,59),(11,'Koncert Żabson','2022-02-19 19:30:00',4500,0,7,0,0,0,5,79),(12,'Koncert Tymek','2022-03-05 19:30:00',4500,0,7,0,0,0,3,79),(13,'Kombii na STADIONIE NARODOWYM','2022-02-11 19:30:00',45000,0,6,0,0,0,10,12.49),(14,'Tommy Cash we Wrocławiu','2022-03-12 20:30:00',1500,0,5,0,0,0,11,149),(15,'Young Multi Koncert w VRze','2022-02-11 17:00:00',15000,0,4,0,0,0,12,1),(16,'Rogal Narodowy','2022-02-25 21:30:00',45000,0,6,0,0,0,13,120),(17,'Wielkie POGO','2022-03-05 12:00:00',5000,0,10,0,0,0,8,1),(18,'Wielkie POGO 2','2022-03-05 12:30:00',5000,0,10,0,0,0,14,1),(20,'Kwiat Jabłoni w Poznaniu','2022-02-19 19:00:00',4500,0,8,0,0,0,15,59);
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `lid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `capacity` int NOT NULL DEFAULT '0',
  `address` varchar(100) NOT NULL,
  `indoor` tinyint NOT NULL DEFAULT '1',
  `cid` int NOT NULL,
  PRIMARY KEY (`lid`),
  UNIQUE KEY `id_UNIQUE` (`lid`),
  KEY `fk_locations_cities_idx` (`cid`),
  CONSTRAINT `fk_locations_cities` FOREIGN KEY (`cid`) REFERENCES `cities` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'Klub Studio',2500,'Witolda Budryka 4, 30-072 Kraków',1,1),(2,'Klub Kwadrat',1500,'Stanisława Skarżyńskiego 1, 31-866 Kraków',1,1),(3,'Tauron Arena',15000,'Stanisława Lema 7, 31-571 Kraków',1,1),(4,'Muzeum Lotnictwa Polskiego',15000,'al. Jana Pawła II 39, 31-864 Kraków',0,1),(5,'Centrum Koncertowe A4',1500,'Robotnicza 42D, 53-608 Wrocław',1,2),(6,'Stadion Narodowy',45000,'al. Księcia Józefa Poniatowskiego 1, 03-901 Warszawa',1,3),(7,'COS Torwar',4500,'Łazienkowska 6A, 00-449 Warszawa',1,3),(8,'Klub Muzyczny B17',4500,'Bułgarska 17, 60-381 Poznań\r\n',1,4),(9,' Kampus Wielicki',1500,'ul. Józefa Piłsudskiego 105 Wieliczka\r\n',1,5),(10,'Miasteczko Studenckie AGH',5000,'Józefa Rostafińskiego 7a, 30-072 Kraków',0,1);
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets` (
  `tid` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `eid` int NOT NULL,
  PRIMARY KEY (`tid`,`uid`,`eid`),
  KEY `fk_tickets_users1_idx` (`uid`),
  KEY `fk_tickets_events1_idx` (`eid`),
  CONSTRAINT `fk_tickets_events1` FOREIGN KEY (`eid`) REFERENCES `events` (`eid`),
  CONSTRAINT `fk_tickets_users1` FOREIGN KEY (`uid`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(145) NOT NULL,
  `email` varchar(45) NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `balance` double NOT NULL DEFAULT '0',
  `phone_number` varchar(12) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idusers_UNIQUE` (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-11 12:38:05
