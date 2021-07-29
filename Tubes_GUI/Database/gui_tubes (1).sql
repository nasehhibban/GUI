-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 29 Jul 2021 pada 17.04
-- Versi server: 10.4.14-MariaDB
-- Versi PHP: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gui_tubes`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `developer`
--

CREATE TABLE `developer` (
  `DeveloperID` int(11) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Alamat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `developer`
--

INSERT INTO `developer` (`DeveloperID`, `Nama`, `Email`, `Alamat`) VALUES
(0, '', '', ''),
(21, 'asdsd', 'asd', 'asdd'),
(102, 'Hanas', 'aaaa@gmail', 'Kebumen'),
(109, 'Iqbal', 'Iqbal001@gmail', 'Losari'),
(221, 'Hell', 'Hell@gmail', 'Purwokerto'),
(224, 'Lala', 'Poio@gmail', 'Semarang');

-- --------------------------------------------------------

--
-- Struktur dari tabel `game`
--

CREATE TABLE `game` (
  `GameID` int(11) NOT NULL,
  `Nama_Game` varchar(100) NOT NULL,
  `Genre` varchar(50) NOT NULL,
  `Tahun_rilis` int(11) NOT NULL,
  `Harga` int(11) NOT NULL,
  `Deskripsi` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `game`
--

INSERT INTO `game` (`GameID`, `Nama_Game`, `Genre`, `Tahun_rilis`, `Harga`, `Deskripsi`) VALUES
(123, 'sfdf', 'sdf', 23123, 1233, 'dsacac'),
(401, 'Adios', 'Horror', 2021, 50000, 'Game ini adalah Game horror'),
(889, 'Lama Timen', 'Adventure', 2021, 10000000, 'Game ini adalah game keren');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pembeli`
--

CREATE TABLE `pembeli` (
  `PembeliID` int(11) NOT NULL,
  `NickName` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `NoTelp` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pembeli`
--

INSERT INTO `pembeli` (`PembeliID`, `NickName`, `Email`, `Password`, `NoTelp`) VALUES
(0, 'Dea', 'lilu@gmail', 'sasasa', 34274624),
(101, 'Delon717', 'lealea@gmail', 'sapisapian', 87653647833),
(102, 'Ase', 'lala@gmail', 'sasa', 987564),
(103, 'Abi', 'io@gmail', 'lue', 987653737),
(104, 'fa', 'hg@gmail', 'seraa', 909876576),
(122, 'shania', 'jajsaj', 'sasa', 98373434),
(167, 'Rapshody', 'Lialala@gmail', 'sapi', 9837264);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `developer`
--
ALTER TABLE `developer`
  ADD PRIMARY KEY (`DeveloperID`);

--
-- Indeks untuk tabel `game`
--
ALTER TABLE `game`
  ADD PRIMARY KEY (`GameID`);

--
-- Indeks untuk tabel `pembeli`
--
ALTER TABLE `pembeli`
  ADD PRIMARY KEY (`PembeliID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
