<?php

Class Calculator {

	private $number1;
	private $number2;
	private $operator;
	
	public function setNumber1($number1){
		$this->number1 = $number1;
	}
	
	public function setNumber2($number2){
		$this->number2 = $number2;
	}
	
	public function setOperator($operator){
		$this->operator = $operator;
	}

	private function addition(){
		return $this->number1 + $this->number2;
	}

	private function subtration(){
		return $this->number1 - $this->number2;
	}

	private function multiplication(){
		return $this->number1 * $this->number2;
	}

	private function division(){
		return $this->number1 / $this->number2;
	}

	public function verifyOperator(){
		switch($this->operator){
			case '+':
				return $this->addition();
				break;
			case '-':
				return $this->subtration();
				break;
			case '*':
				return $this->multiplication();
				break;
			case '/':
				return $this->division();
				break;
			default:
				return "Operation not defined!";
				break;
		}

	}
}

?>