#include "Concert.h"
#include <iostream>

int main(int argc, char** argv){

	//declare all of the Concerts
	Concert c1, c2, c3, c4, c5, c6, c7, c8, c9, c10;
	
	//Filling them all with data.
	c1.setConcertName("Spooky Sings");
	c1.setDesire(10);
	c1.setDate(2000, 10, 31);
	c1.setFriend("Jeff");
	c1.setFriend("Jeoff");

	c2.setDate(1999, 11, 23);
	c2.setConcertName("Turkey Troubles");
	c2.setDesire(4);
	c2.setFriend(c1.getFriends()[0]);
	c2.setFriend("Tom");

	c3 = Concert("Jesus Jamz", c1.getFriends(), 3, c1.getDate());
	c3.setFriend("Christian");
	c3.setDate(1999, 12, 25);

	c4.setConcertName("New Year New Me");
	c4.setDesire(9);
	c4.setDate(1998, 1, 1);
	c4.setFriend("Jack");
	c4.setFriend("Daniels");

	c5 = Concert("May The Fourth", c1.getFriends(), 9, c2.getDate());
	c5.setFriend("Obi-Wan");
	c5.setDate(2007, 5, 4);

	c6.setConcertName("Be With You");
	c6.setDesire(7);
	c6.setDate(2007, 5, 4);
	c6.setFriend("Luke");
	c6.setFriend("Leia");

	c7 = Concert("Hannukah Happiness", c1.getFriends(), 10, c3.getDate());
	c7.setFriend("Moses");

	c8 = Concert("Irish Potato Festival", c1.getFriends(), 10, c6.getDate());
	c8.setFriend("Seamous");
	c8.setDate(2017, 3, 17);

	c9.setConcertName("American Invaders Day");
	c9.setDesire(6);
	c9.setDate(2004, 10, 9);
	c9.setFriend(c8.getFriends()[1]);
	c9.setFriend("Christopher");

	c10 = Concert("Bob Dylan Concert", c8.getFriends(), 10, c7.getDate());
	c10.setFriend("Bob");
	
	//create the vector holding them all.
	std::vector<Concert::Concert> concerts = {c1,c2,c3,c4,c5,c6,c7,c8,c9,c10};

	//sort them.
	std::sort(concerts.begin(), concerts.end());//cpp reference .com

	//loop through and print them all sorted.
	for(int i=0;i<concerts.size();i++){
		std::cout << "\nConcert: " << i+1;
		std::cout << concerts[i] << std::endl;
	}		
}
