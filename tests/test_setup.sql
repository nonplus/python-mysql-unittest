-- Initialize Student table
DROP TABLE IF EXISTS Student;
CREATE TABLE `Student` (
    `ID` int NOT NULL AUTO_INCREMENT,
    `Name` varchar(45) NOT NULL,
    `DOB` date NOT NULL,
    `Grade` int NOT NULL,
    `GPA` decimal(6,5) DEFAULT NULL,
    PRIMARY KEY (`ID`)
    ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Note: Use ENGINE=MEMORY for better test performance
