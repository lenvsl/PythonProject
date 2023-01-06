-- MariaDB dump 10.17  Distrib 10.4.14-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.4.14-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `arrivalsgreeceforeign`
--

DROP TABLE IF EXISTS `arrivalsgreeceforeign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arrivalsgreeceforeign` (
  `Time` int(4) DEFAULT NULL,
  `Geo` varchar(255) DEFAULT NULL,
  `Value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arrivalsgreeceforeign`
--

LOCK TABLES `arrivalsgreeceforeign` WRITE;
/*!40000 ALTER TABLE `arrivalsgreeceforeign` DISABLE KEYS */;
INSERT INTO `arrivalsgreeceforeign` VALUES (2010,'Greece',23980309.040000003),(2011,'Greece',26674961.509999998),(2012,'Greece',24447526.86),(2013,'Greece',27758142.39);
/*!40000 ALTER TABLE `arrivalsgreeceforeign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arrivalsgreecetotal`
--

DROP TABLE IF EXISTS `arrivalsgreecetotal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arrivalsgreecetotal` (
  `Time` int(4) DEFAULT NULL,
  `Geo` varchar(255) DEFAULT NULL,
  `Value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arrivalsgreecetotal`
--

LOCK TABLES `arrivalsgreecetotal` WRITE;
/*!40000 ALTER TABLE `arrivalsgreecetotal` DISABLE KEYS */;
INSERT INTO `arrivalsgreecetotal` VALUES (2010,'Greece',44508442.70999999),(2011,'Greece',45359471.43000001),(2012,'Greece',40134783.7),(2013,'Greece',44336865.70999999);
/*!40000 ALTER TABLE `arrivalsgreecetotal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arrivalsitalyforeign`
--

DROP TABLE IF EXISTS `arrivalsitalyforeign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arrivalsitalyforeign` (
  `Time` int(4) DEFAULT NULL,
  `Geo` varchar(255) DEFAULT NULL,
  `Value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arrivalsitalyforeign`
--

LOCK TABLES `arrivalsitalyforeign` WRITE;
/*!40000 ALTER TABLE `arrivalsitalyforeign` DISABLE KEYS */;
INSERT INTO `arrivalsitalyforeign` VALUES (2010,'Italy',96362622.68999998),(2011,'Italy',104398833.64),(2012,'Italy',107348223.40999998),(2013,'Italy',110800540.9);
/*!40000 ALTER TABLE `arrivalsitalyforeign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arrivalsitalytotal`
--

DROP TABLE IF EXISTS `arrivalsitalytotal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arrivalsitalytotal` (
  `Time` int(4) DEFAULT NULL,
  `Geo` varchar(255) DEFAULT NULL,
  `Value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arrivalsitalytotal`
--

LOCK TABLES `arrivalsitalytotal` WRITE;
/*!40000 ALTER TABLE `arrivalsitalytotal` DISABLE KEYS */;
INSERT INTO `arrivalsitalytotal` VALUES (2010,'Italy',217067400.35999998),(2011,'Italy',228115866.20999998),(2012,'Italy',228554692.75),(2013,'Italy',228948354.6);
/*!40000 ALTER TABLE `arrivalsitalytotal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nightsgreeceforeign`
--

DROP TABLE IF EXISTS `nightsgreeceforeign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nightsgreeceforeign` (
  `Time` int(4) DEFAULT NULL,
  `Geo` varchar(255) DEFAULT NULL,
  `Value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nightsgreeceforeign`
--

LOCK TABLES `nightsgreeceforeign` WRITE;
/*!40000 ALTER TABLE `nightsgreeceforeign` DISABLE KEYS */;
INSERT INTO `nightsgreeceforeign` VALUES (2010,'Greece',127236365.27),(2011,'Greece',140205446.8),(2012,'Greece',132623672.95),(2013,'Greece',149919791.54000002);
/*!40000 ALTER TABLE `nightsgreeceforeign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nightsgreecetotal`
--

DROP TABLE IF EXISTS `nightsgreecetotal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nightsgreecetotal` (
  `Time` int(4) DEFAULT NULL,
  `Geo` varchar(255) DEFAULT NULL,
  `Value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nightsgreecetotal`
--

LOCK TABLES `nightsgreecetotal` WRITE;
/*!40000 ALTER TABLE `nightsgreecetotal` DISABLE KEYS */;
INSERT INTO `nightsgreecetotal` VALUES (2010,'Greece',186768309.98),(2011,'Greece',193301650.45000002),(2012,'Greece',178653208.04),(2013,'Greece',197259655.98);
/*!40000 ALTER TABLE `nightsgreecetotal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nightsitalyforeign`
--

DROP TABLE IF EXISTS `nightsitalyforeign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nightsitalyforeign` (
  `Time` int(4) DEFAULT NULL,
  `Geo` varchar(255) DEFAULT NULL,
  `Value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nightsitalyforeign`
--

LOCK TABLES `nightsitalyforeign` WRITE;
/*!40000 ALTER TABLE `nightsitalyforeign` DISABLE KEYS */;
INSERT INTO `nightsitalyforeign` VALUES (2010,'Italy',384056026.07000005),(2011,'Italy',409408234.85999995),(2012,'Italy',419084682.7),(2013,'Italy',428049914.8);
/*!40000 ALTER TABLE `nightsitalyforeign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nightsitalytotal`
--

DROP TABLE IF EXISTS `nightsitalytotal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nightsitalytotal` (
  `Time` int(4) DEFAULT NULL,
  `Geo` varchar(255) DEFAULT NULL,
  `Value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nightsitalytotal`
--

LOCK TABLES `nightsitalytotal` WRITE;
/*!40000 ALTER TABLE `nightsitalytotal` DISABLE KEYS */;
INSERT INTO `nightsitalytotal` VALUES (2010,'Italy',875536869.1399999),(2011,'Italy',900781257.9999999),(2012,'Italy',886532073.2199999),(2013,'Italy',875605147.7);
/*!40000 ALTER TABLE `nightsitalytotal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-12 14:08:04
