create table stock(
    `code` char(10) not null comment "股票代码",
    `name` char(50) not null comment "股票名称",
    `link` char(50) not null comment "股票链接",
    `forum` char(50) not null comment "股吧链接",
    `money_stream` char(50) not null comment "资金流",
    `data` char(50) not null comment "数据",
    `price` char(10) not null comment "价格",
    `range` char(10) not null comment "涨跌幅",
    `increment` char(10) not null comment "增长量",
    `turnover` char(10) not null comment "成交量",
    `turnvolume` char(10) not null comment "成交额",
    `amplitude` char(10) not null comment "振幅",
    `highest` char(10) not null comment "最高",
    `lowest` char(10) not null comment "最低",
    `begin` char(10) not null comment "今开",
    `history` char(10) not null comment "昨收",
    `volume_rate` char(10) not null comment "量比",
    `turnover_rate` char(10) not null comment "换手率",
    `pe_rate` char(10) not null comment "市盈率",
    `market_rate` char(10) not null comment "市净率"
);

create table ip_pool
(
    `ip`      char(20) not null,
    `address` char(50) default null,
    `type`    char(20) default null,
    `source`  char(20) default null,
    `website` tinyint(2) not null
);