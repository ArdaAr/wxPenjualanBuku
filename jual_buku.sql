-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 18, 2021 at 03:05 PM
-- Server version: 10.4.16-MariaDB
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jual_buku`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ID_Admin` int(11) NOT NULL,
  `Nama_Admin` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`ID_Admin`, `Nama_Admin`, `username`, `password`) VALUES
(1, 'dokoke kokeye', 'dokoke', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `id_buku` int(11) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `id_kategori` int(11) NOT NULL,
  `harga` int(11) NOT NULL,
  `penerbit` varchar(50) NOT NULL,
  `stok` int(11) NOT NULL,
  `gambar` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`id_buku`, `judul`, `id_kategori`, `harga`, `penerbit`, `stok`, `gambar`) VALUES
(1, 'Kambing Jantan', 2, 80000, 'Gagas Media', 10, 'kambingjantan.jpg'),
(2, 'Teori Relativitas', 1, 100000, 'Penerbit Luar', 9, 'relativitas.jpg'),
(3, 'Naruto', 4, 50000, 'Konoha Cetak', 10, 'naruto.jpg'),
(4, 'Si Kancil', 2, 20000, 'Buat Sendiri', 45, 'kancil.jpg'),
(6, 'Chord Lagu', 1, 15000, 'Koran Musik', 43, 'chord.jpg'),
(7, 'Ternak Lele', 1, 40000, 'Cetak Sendiri', 10, 'lele.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id_user` int(11) NOT NULL,
  `Nama_Customer` varchar(30) NOT NULL,
  `Alamat` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `telepon` varchar(30) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `foto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id_user`, `Nama_Customer`, `Alamat`, `email`, `telepon`, `username`, `password`, `foto`) VALUES
(1, 'Ijul ', 'Desa Penambangan Kecamatan Semanding', 'ijul@gmail.com', '081234567890', 'izzulfaiz', '123', 'izzul.bmp'),
(2, 'ardana', 'semanding', 'arda@gmail.com', '081234565541', 'ardaar', '12345', 'arda.jpg'),
(3, 'durajak', 'perunggahan', 'drj@gmail.com', '087945612341', 'durs', '1234', 'durs.png'),
(5, 'supri', 'Tuban', 'supri@gmail.com', '0214567845', 'supri', '123', ''),
(6, '', '', '', '', '', '', ''),
(7, 'Kaiju', 'Tuban', 'kaiju@gmail.com', '08154462125', 'kaiju', '123', ''),
(8, 'andy', 'Tuban jawa timur', 'andy', '0812154612', 'andy', '123', '');

-- --------------------------------------------------------

--
-- Table structure for table `kategori`
--

CREATE TABLE `kategori` (
  `id_kategori` int(11) NOT NULL,
  `kategori` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kategori`
--

INSERT INTO `kategori` (`id_kategori`, `kategori`) VALUES
(1, 'Pendidikan'),
(2, 'Komedi'),
(3, 'Cinta'),
(4, 'Petualangan');

-- --------------------------------------------------------

--
-- Table structure for table `pesanan`
--

CREATE TABLE `pesanan` (
  `id_pesanan` int(11) NOT NULL,
  `id_customer` int(11) NOT NULL,
  `id_buku` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `tanggal` datetime NOT NULL DEFAULT current_timestamp(),
  `total_harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pesanan`
--

INSERT INTO `pesanan` (`id_pesanan`, `id_customer`, `id_buku`, `quantity`, `tanggal`, `total_harga`) VALUES
(1, 2, 3, 20, '0000-00-00 00:00:00', 100000),
(2, 1, 3, 2, '2021-05-31 00:59:59', 100000),
(3, 1, 3, 3, '2021-05-31 10:58:39', 190000),
(4, 1, 3, 2, '2021-05-31 11:11:59', 100000),
(5, 1, 1, 5, '2021-05-31 11:14:08', 400000),
(6, 1, 1, 5, '2021-05-31 11:38:24', 400000),
(7, 1, 4, 10, '2021-05-31 11:48:52', 200000),
(8, 2, 7, 5, '2021-05-31 12:34:10', 200000),
(9, 1, 1, 2, '2021-05-31 14:43:22', 190000),
(10, 1, 6, 2, '2021-05-31 14:43:24', 190000),
(11, 1, 4, 5, '2021-05-31 14:46:47', 100000),
(12, 1, 3, 3, '2021-05-31 14:52:53', 150000),
(13, 1, 2, 2, '2021-06-01 20:45:01', 450000),
(14, 1, 3, 5, '2021-06-01 20:45:02', 450000),
(15, 2, 1, 3, '2021-06-02 11:44:07', 240000),
(16, 1, 1, 5, '2021-06-04 19:51:38', 600000),
(17, 1, 2, 2, '2021-06-04 19:51:40', 600000),
(18, 1, 1, 1, '2021-06-04 20:05:48', 80000),
(19, 7, 6, 10, '2021-06-04 20:16:40', 650000),
(20, 7, 2, 5, '2021-06-04 20:16:42', 650000),
(21, 8, 1, 5, '2021-06-04 21:40:41', 475000),
(22, 8, 6, 5, '2021-06-04 21:40:43', 475000),
(23, 8, 1, 5, '2021-06-04 21:53:33', 600000),
(24, 8, 2, 2, '2021-06-04 21:53:35', 600000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID_Admin`);

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id_buku`),
  ADD KEY `id_kategori` (`id_kategori`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id_user`);

--
-- Indexes for table `kategori`
--
ALTER TABLE `kategori`
  ADD PRIMARY KEY (`id_kategori`);

--
-- Indexes for table `pesanan`
--
ALTER TABLE `pesanan`
  ADD PRIMARY KEY (`id_pesanan`),
  ADD KEY `id_customer` (`id_customer`),
  ADD KEY `id_buku` (`id_buku`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID_Admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `buku`
  MODIFY `id_buku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `kategori`
--
ALTER TABLE `kategori`
  MODIFY `id_kategori` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `pesanan`
--
ALTER TABLE `pesanan`
  MODIFY `id_pesanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `buku`
--
ALTER TABLE `buku`
  ADD CONSTRAINT `buku_ibfk_1` FOREIGN KEY (`id_kategori`) REFERENCES `kategori` (`id_kategori`);

--
-- Constraints for table `pesanan`
--
ALTER TABLE `pesanan`
  ADD CONSTRAINT `pesanan_ibfk_1` FOREIGN KEY (`id_customer`) REFERENCES `customer` (`id_user`),
  ADD CONSTRAINT `pesanan_ibfk_2` FOREIGN KEY (`id_buku`) REFERENCES `buku` (`id_buku`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
