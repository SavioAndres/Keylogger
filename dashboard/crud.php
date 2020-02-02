<?php 

namespace App\Dashboard;

use App\Dashboard\Connect;

class Crud extends Connect
{
    private $table;

    public function __construct(string $table = null)
    {
        $this->table = $table;
    }

    public function readAllTable(string $attributes = '*', string $order = ''): array
    {
        $stmt = Connect::connect()->prepare('SELECT ' . $attributes . ' FROM ' . $this->table . ' ' . $order);
        $stmt->execute();
        return $stmt->fetchAll(\PDO::FETCH_ASSOC);
    }
}