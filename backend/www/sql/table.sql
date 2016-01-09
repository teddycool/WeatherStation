CREATE TABLE IF NOT EXISTS `ws_data_shortterm` (
  `id` int(11) NOT NULL,
  `servertime` datetime NOT NULL,
  `measuretime` datetime NOT NULL,
  `fridgetemphigh` float NOT NULL,
  `fridgetemplow` float NOT NULL,
  `freezertemp` float NOT NULL,
  `outdoortemp` float NOT NULL,
  `indoortemp` float NOT NULL,
  `outdoorhum` float NOT NULL,
  `indoorhum` float NOT NULL,
  `outdoorbar` float NOT NULL,
  `irlight` float NOT NULL,
  `amblight` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


ALTER TABLE `ws_data_shortterm`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `ws_data_shortterm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


--- add light and ir... 