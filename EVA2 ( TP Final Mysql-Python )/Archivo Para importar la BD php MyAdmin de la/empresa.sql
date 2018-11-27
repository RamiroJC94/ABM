-- phpMyAdmin SQL Dump
-- version 2.10.3
-- http://www.phpmyadmin.net
-- 
-- Servidor: localhost
-- Tiempo de generación: 21-11-2013 a las 19:57:40
-- Versión del servidor: 5.0.51
-- Versión de PHP: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

-- 
-- Base de datos: `empresa`
-- 

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `alta_proyect`
-- 

CREATE TABLE `alta_proyect` (
  `ID_alta_Proyect` int(10) NOT NULL,
  `ID_Proyecto` int(11) NOT NULL,
  `Legajo` int(11) NOT NULL,
  PRIMARY KEY  (`ID_alta_Proyect`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- 
-- Volcar la base de datos para la tabla `alta_proyect`
-- 

INSERT INTO `alta_proyect` VALUES (0, 1, 1);

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `alta_recursos`
-- 

CREATE TABLE `alta_recursos` (
  `ID_Alta_Proyect` int(11) NOT NULL,
  `ID_Proyect` int(11) NOT NULL,
  `ID_Recursos` int(11) NOT NULL,
  PRIMARY KEY  (`ID_Alta_Proyect`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- 
-- Volcar la base de datos para la tabla `alta_recursos`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `clientes`
-- 

CREATE TABLE `clientes` (
  `ID_Cliente` int(10) unsigned NOT NULL auto_increment,
  `nombre` varchar(15) NOT NULL,
  `fecha_init` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`ID_Cliente`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

-- 
-- Volcar la base de datos para la tabla `clientes`
-- 

INSERT INTO `clientes` VALUES (1, 'Nelson', '2013-11-15 12:38:25');
INSERT INTO `clientes` VALUES (2, 'IEEE', '2013-11-15 12:42:01');
INSERT INTO `clientes` VALUES (3, 'carlos', '2013-11-15 12:43:44');
INSERT INTO `clientes` VALUES (4, 'emanuel', '2013-11-15 12:43:44');
INSERT INTO `clientes` VALUES (5, 'federico', '2013-11-15 12:43:44');
INSERT INTO `clientes` VALUES (6, 'paez', '2013-11-15 12:43:44');
INSERT INTO `clientes` VALUES (7, 'Sofi', '2013-11-15 12:43:44');
INSERT INTO `clientes` VALUES (8, 'Laura', '2013-11-15 12:43:44');
INSERT INTO `clientes` VALUES (9, 'Ary', '2013-11-15 12:43:44');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `facturas_p`
-- 

CREATE TABLE `facturas_p` (
  `N°_factura` int(10) unsigned NOT NULL auto_increment,
  `ID_Proyect` int(11) NOT NULL,
  `Monto` int(14) NOT NULL,
  `Descrip_Hito` varchar(40) NOT NULL,
  `estado` varchar(12) default NULL,
  `fecha_emicion` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `fecha_pago` time default NULL,
  PRIMARY KEY  (`N°_factura`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `facturas_p`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `facturas_r`
-- 

CREATE TABLE `facturas_r` (
  `N°_factura` int(10) unsigned NOT NULL auto_increment,
  `Monto` int(14) NOT NULL,
  `estado` varchar(12) default NULL,
  `fecha_emicion` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `fecha_pago` time default NULL,
  PRIMARY KEY  (`N°_factura`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `facturas_r`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `historial`
-- 

CREATE TABLE `historial` (
  `ID_Mod` int(10) unsigned NOT NULL auto_increment,
  `ID_Proyect` int(11) NOT NULL,
  `Descripcion` varchar(50) NOT NULL,
  `fecha_Mod` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`ID_Mod`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `historial`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `proveedores`
-- 

CREATE TABLE `proveedores` (
  `ID_Proveedor` int(10) unsigned NOT NULL auto_increment,
  `nombre` varchar(15) NOT NULL,
  `fecha_init` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`ID_Proveedor`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `proveedores`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `proyects`
-- 

CREATE TABLE `proyects` (
  `ID_Proyecto` int(10) unsigned NOT NULL auto_increment,
  `nombre` varchar(15) NOT NULL,
  `responsable` varchar(15) NOT NULL,
  `fecha_init` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `estado` varchar(15) NOT NULL,
  `Type_Proyect` varchar(15) NOT NULL,
  PRIMARY KEY  (`ID_Proyecto`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `proyects`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `recursos`
-- 

CREATE TABLE `recursos` (
  `Id` int(10) unsigned NOT NULL auto_increment,
  `Descripcion` varchar(30) NOT NULL,
  `Monto` int(14) NOT NULL,
  `fecha_entrega` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `costo_mensual` int(14) NOT NULL,
  `estado` varchar(12) default NULL,
  `comprado` tinyint(1) NOT NULL default '0',
  PRIMARY KEY  (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `recursos`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `recursos_h`
-- 

CREATE TABLE `recursos_h` (
  `Legajo` int(10) unsigned NOT NULL auto_increment,
  `nombre` varchar(15) NOT NULL,
  `apellido` varchar(15) NOT NULL,
  `posicion` varchar(12) NOT NULL,
  `salario` int(7) NOT NULL,
  `fecha_init` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`Legajo`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `recursos_h`
-- 

