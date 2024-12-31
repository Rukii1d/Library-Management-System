-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 18, 2024 at 12:36 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_Id` int(11) NOT NULL,
  `user_Id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_Id`, `user_Id`) VALUES
(1001, 1),
(1002, 2);

-- --------------------------------------------------------

--
-- Table structure for table `author`
--

CREATE TABLE `author` (
  `author_Id` int(11) NOT NULL,
  `author_name` varchar(255) NOT NULL,
  `author_subject` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `author`
--

INSERT INTO `author` (`author_Id`, `author_name`, `author_subject`) VALUES
(1, 'Harper Lee', 'Social Justice'),
(2, 'George Orwell', 'Totalitarianism'),
(3, 'Scott Fitzgerald', 'Social Commentary'),
(4, 'J.D. Salinger', 'Teenage angst'),
(5, 'J.R.R. Tolkien', 'Fantacy');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_Id` int(11) NOT NULL,
  `book_name` varchar(255) NOT NULL,
  `book_price` decimal(10,2) NOT NULL,
  `genre_Id` int(11) NOT NULL,
  `publisher_code` int(11) NOT NULL,
  `author_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_Id`, `book_name`, `book_price`, `genre_Id`, `publisher_code`, `author_Id`) VALUES
(1, 'To Kill A Moking Bird', 500.00, 1, 11, 1),
(2, '1984', 700.00, 2, 22, 2),
(3, 'The Grade Gatsby', 550.00, 3, 33, 3),
(4, 'The Catcher In The Right', 750.00, 4, 44, 4),
(5, 'The Hobbit', 1050.00, 5, 55, 5);

-- --------------------------------------------------------

--
-- Table structure for table `borrowed_books`
--

CREATE TABLE `borrowed_books` (
  `borrower_Id` int(11) NOT NULL,
  `book_Id` int(11) NOT NULL,
  `issue_date` date NOT NULL,
  `return_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrowed_books`
--

INSERT INTO `borrowed_books` (`borrower_Id`, `book_Id`, `issue_date`, `return_date`) VALUES
(1, 1, '2023-04-05', '2023-04-12'),
(1, 4, '2023-04-15', '2023-04-22'),
(2, 1, '2023-10-12', NULL),
(2, 2, '2023-04-08', '2023-04-15'),
(3, 1, '2023-10-15', NULL),
(3, 3, '2023-04-12', '2023-04-20'),
(4, 3, '2023-10-15', NULL),
(4, 4, '2023-04-12', '2023-04-20'),
(5, 1, '2023-04-15', '2023-04-22'),
(5, 2, '2023-12-15', NULL),
(5, 4, '2023-04-11', '2023-04-19'),
(6, 1, '2023-12-25', '2023-12-28'),
(7, 1, '2023-12-26', '2023-12-29'),
(8, 4, '2023-12-26', '2023-12-30'),
(9, 4, '2023-12-26', '2023-12-30'),
(10, 1, '2023-12-22', '2023-12-30'),
(10, 2, '2023-12-26', '2023-12-30'),
(10, 3, '2023-12-22', '2023-12-30');

--
-- Triggers `borrowed_books`
--
DELIMITER $$
CREATE TRIGGER `check_available_books` BEFORE INSERT ON `borrowed_books` FOR EACH ROW BEGIN
    IF (SELECT available_copies FROM books WHERE book_Id = NEW.book_Id) <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Book is not available for borrowing.';
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `borrower`
--

CREATE TABLE `borrower` (
  `borrower_Id` int(11) NOT NULL,
  `borrower_name` varchar(255) NOT NULL,
  `contact_no` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `DOB` date NOT NULL,
  `user_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrower`
--

INSERT INTO `borrower` (`borrower_Id`, `borrower_name`, `contact_no`, `address`, `DOB`, `user_Id`) VALUES
(1, 'Malintha', '070909777', 'N0.50,Kandy road,Kundasale', '1990-01-01', 5),
(2, 'Theekshana', '0709877279', 'N0.60,Badulla road,Kundasale', '1980-02-21', 1),
(3, 'Avishka', '0712345679', 'N0.10,Katugasthota road,Kundasale', '2000-04-21', 2),
(4, 'Kanchana', '0789098786', 'N0.70,Dambulla road,Kundasale', '2000-08-11', 3),
(5, 'Praneeth', '078909777', 'N0.80,Katunayake road,Kundasale', '2001-01-24', 4),
(6, 'Nimal', '07745643', 'NO:50,Kandy road,Dambulla', '1990-10-28', 6),
(7, 'Kamal', '07745643', 'NO:60,Kandy road,Dambulla', '1992-12-08', 7),
(8, 'Jhone', ' 07134567', 'NO:80,Mathale road,Dambulla', '2002-05-08', 8),
(9, 'Shane', ' 076890865', 'NO:10,Digana road,Teldeniya', '2000-09-12', 9),
(10, 'Shane', ' 076890865', 'NO:10,Digana road,Kundasale', '2000-09-13', 10);

-- --------------------------------------------------------

--
-- Table structure for table `b_orrower`
--

CREATE TABLE `b_orrower` (
  `Bcard_Id` int(11) NOT NULL,
  `user_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `b_orrower`
--

INSERT INTO `b_orrower` (`Bcard_Id`, `user_Id`) VALUES
(101, 1),
(102, 2),
(103, 3),
(104, 4),
(105, 5);

-- --------------------------------------------------------

--
-- Table structure for table `genre`
--

CREATE TABLE `genre` (
  `genre_Id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `genre`
--

INSERT INTO `genre` (`genre_Id`, `title`) VALUES
(1, 'Fiction'),
(2, 'Dystopian fiction'),
(3, 'Classic Literature'),
(4, 'Coming of age Fiction'),
(5, 'Advanture and Mythology');

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `publisher_code` int(11) NOT NULL,
  `publisher_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `publisher`
--

INSERT INTO `publisher` (`publisher_code`, `publisher_name`) VALUES
(11, 'J.B.Lippincott & co.'),
(22, 'Secker & Warburg'),
(33, 'Charles Scribner\'s Sons'),
(44, 'Little brown and Company'),
(55, 'George allen and Unwin');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_Id` int(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `contact_no` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_Id`, `user_name`, `contact_no`) VALUES
(1, 'Theekshana', '0709877279'),
(2, 'Avishka', '0712345679'),
(3, 'Kanchana', '0789098786'),
(4, 'Praneeth', '078909777'),
(5, 'Malintha', '070909777'),
(6, 'Nimal', '07745643'),
(7, 'Kamal', '07745643'),
(8, 'Jhone', '07134567'),
(9, 'Shane', '076890865'),
(10, 'Danial', '074098746');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_Id`),
  ADD KEY `user_Id` (`user_Id`);

--
-- Indexes for table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`author_Id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_Id`),
  ADD KEY `genre_Id` (`genre_Id`),
  ADD KEY `publisher_code` (`publisher_code`),
  ADD KEY `author_Id` (`author_Id`);

--
-- Indexes for table `borrowed_books`
--
ALTER TABLE `borrowed_books`
  ADD PRIMARY KEY (`borrower_Id`,`book_Id`),
  ADD KEY `book_Id` (`book_Id`);

--
-- Indexes for table `borrower`
--
ALTER TABLE `borrower`
  ADD PRIMARY KEY (`borrower_Id`),
  ADD KEY `user_Id` (`user_Id`);

--
-- Indexes for table `b_orrower`
--
ALTER TABLE `b_orrower`
  ADD PRIMARY KEY (`Bcard_Id`),
  ADD KEY `user_Id` (`user_Id`);

--
-- Indexes for table `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`genre_Id`);

--
-- Indexes for table `publisher`
--
ALTER TABLE `publisher`
  ADD PRIMARY KEY (`publisher_code`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1003;

--
-- AUTO_INCREMENT for table `author`
--
ALTER TABLE `author`
  MODIFY `author_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `book_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `borrower`
--
ALTER TABLE `borrower`
  MODIFY `borrower_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `b_orrower`
--
ALTER TABLE `b_orrower`
  MODIFY `Bcard_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- AUTO_INCREMENT for table `genre`
--
ALTER TABLE `genre`
  MODIFY `genre_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `publisher`
--
ALTER TABLE `publisher`
  MODIFY `publisher_code` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`user_Id`) REFERENCES `user` (`user_Id`) ON DELETE CASCADE;

--
-- Constraints for table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`genre_Id`) REFERENCES `genre` (`genre_Id`),
  ADD CONSTRAINT `books_ibfk_2` FOREIGN KEY (`publisher_code`) REFERENCES `publisher` (`publisher_code`),
  ADD CONSTRAINT `books_ibfk_3` FOREIGN KEY (`author_Id`) REFERENCES `author` (`author_Id`);

--
-- Constraints for table `borrowed_books`
--
ALTER TABLE `borrowed_books`
  ADD CONSTRAINT `borrowed_books_ibfk_1` FOREIGN KEY (`borrower_Id`) REFERENCES `borrower` (`borrower_Id`),
  ADD CONSTRAINT `borrowed_books_ibfk_2` FOREIGN KEY (`book_Id`) REFERENCES `books` (`book_Id`);

--
-- Constraints for table `borrower`
--
ALTER TABLE `borrower`
  ADD CONSTRAINT `borrower_ibfk_1` FOREIGN KEY (`user_Id`) REFERENCES `user` (`user_Id`);

--
-- Constraints for table `b_orrower`
--
ALTER TABLE `b_orrower`
  ADD CONSTRAINT `b_orrower_ibfk_1` FOREIGN KEY (`user_Id`) REFERENCES `user` (`user_Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
