<?php

namespace App\Dashboard;

class Connect
{
    private static $HOST = 'localhost';
    private static $NAME = 'keylogger';
    private static $USER = 'root';
    private static $PASS = '';
    private static $instance = null;

    protected static function connect(): object
    {
        if (is_null(self::$instance)) {
            self::sqlConn();
        }
        return self::$instance;
    }

    protected static function close(): void
    {
        die();
    }

    private static function sqlConn(): void
    {
        try {
            $sql = 'mysql:host=' . self::$HOST . ';dbname=' . self::$NAME . ';charset=utf8';
            self::$instance = new \PDO($sql, self::$USER, self::$PASS);
            self::$instance->setAttribute(\PDO::ATTR_ERRMODE, \PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $exception) {
            die($exception->getMessage());
        }
    }
}