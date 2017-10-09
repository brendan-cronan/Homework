
//#include <stdlib.h>
//#include <string.h>
#include "Concert.h"

Concert::Concert(){
	cName="";
	
	friends.clear();;
	
	desire=0;

	std::tm d1;
	d1.tm_year=2000;
	d1.tm_mon=1;
	d1.tm_mday=1;
	date=d1;
}
Concert::Concert(std::string concertName, std::vector<std::string> friendsList, int _desire, std::tm _date){

	cName=concertName;
	friends=friendsList;
	desire=_desire;
	date=_date;
}

bool Concert::operator<(const Concert& concert)const{
	bool less;
	std::tm d1;
	std::tm d2;
	d1.tm_year=2000;
	d1.tm_mon=2;
	d1.tm_mday=2;

	d2=concert.date;
	int dateComp=compareDates(d1 , d2);
	if(dateComp){//if they are equal
		bool desComp= this->desire - concert.getDesire();//compare the desires 
		if(desComp){//if equal,
			return false;//They are the same so not less than
		}
		else if(desComp>0)//if this one is higher, not less than
			return false;
		else //it is less than.
			return true;
	}
	else if(dateComp>0)//If this one is greater than the other,
		return false;
	else	//else, this one is smaller/
		return true;


}
int Concert::compareDates(std::tm d1, std::tm d2)const{
	int y1=d1.tm_year -1970;
	int y2=d2.tm_year -1970;
	int year= y1 - y2;
	
	int mon = d1.tm_mon - d2.tm_mon;
	
	int day= d1.tm_mday - d2.tm_mday;
	
	int diff;
	diff = year * 365;
	diff += mon * 31;
	diff += day * 1;

	return diff;
}




void Concert::printConcert(){
	std::cout <<	"\nConcert Name: " << cName << std::endl;
	std::cout <<	"List of Freinds Attending: " << std::endl;
	for(int i=0;i<friends.size();i++){
		std::cout << "\t" << friends[i] << "\n";
	}
	std::cout << "Desire to Attend: " << desire << std::endl;
	std::cout << "Date of Event: " << date.tm_mon << "/" << date.tm_mday << "/" << date.tm_year << std::endl;	
}





std::string Concert::getConcertName()const{
	return cName;
}
std::vector<std::string> Concert::getFriends()const{
	return friends;
}
int Concert::getDesire()const{
	return Concert::desire;
}
std::tm Concert::getDate()const{
	return date;
}

void Concert::setConcertName(std::string name){
	cName=name;
}
void Concert::setFriend(std::string friendName){
	friends.push_back(friendName);
}
void Concert::setDesire(int _desire){
	desire=_desire;
}
void Concert::setDate(std::tm _date){
	date=_date;
}
void Concert::setDate(int y,int m,int d){
	date.tm_year=y;
	date.tm_mon=m;
	date.tm_mday=d;
}







