CREATE TABLE `afk` (
  `user` bigint(20) NOT NULL,
  `reason` text,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;