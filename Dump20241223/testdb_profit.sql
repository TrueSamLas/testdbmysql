-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `profit`
--

DROP TABLE IF EXISTS `profit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profit` (
  `idprofit` int NOT NULL AUTO_INCREMENT,
  `ts` timestamp(6) NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `idregister` int NOT NULL,
  `quantite` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `n_profit` decimal(10,2) NOT NULL,
  `rate` decimal(2,2) NOT NULL,
  PRIMARY KEY (`idprofit`),
  KEY `fk_idregister_register_idx` (`idregister`),
  CONSTRAINT `fk_idregister_register` FOREIGN KEY (`idregister`) REFERENCES `register` (`idregister`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profit`
--

LOCK TABLES `profit` WRITE;
/*!40000 ALTER TABLE `profit` DISABLE KEYS */;
INSERT INTO `profit` VALUES (16,'2024-12-06 11:09:23.971576',65,6,12.00,72.00,14.40,0.20),(17,'2024-12-06 11:09:42.752571',66,2,12.00,24.00,4.80,0.20),(18,'2024-12-06 11:10:27.024103',68,2,13.33,26.66,5.33,0.20),(19,'2024-12-11 10:01:10.634398',69,4,13.33,53.32,10.66,0.20),(20,'2024-12-11 10:01:30.896493',70,2,5.50,11.00,2.20,0.20),(22,'2024-12-23 08:45:35.982332',72,1,13.34,13.34,2.67,0.20);
/*!40000 ALTER TABLE `profit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-23 13:38:16
