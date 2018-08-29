package ifal.aspects;

import ifal.classes.MyClass;

public aspect MyAspect {

	pointcut myMethod() : call(
		public void MyClass.myMethod()
	);
    
	before() : myMethod() {
        System.out.println("Antes de executar o meu método!");
    }
	
    after() : myMethod() {
        System.out.println("Depois de executar o meu método!");
    }
	
}
