#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		int fib_cpp();
		void set(int);
	private:
		int age;
		int fib(int);
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}

int Person::fib(int n){
	if (n <= 1){
		return n;
	}
	else{
		return(fib(n-1) + fib(n-2));
	}
	}

int Person::fib_cpp(){
	return fib(age);
	}
 

void Person::set(int n){
	age = n;
	}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	int Person_fib(Person* person) {return person->fib_cpp();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}