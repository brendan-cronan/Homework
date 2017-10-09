#include "Concert.h"
Concert::Concert(){//default Constructor
	cName="";
		
	desire=0;

	std::tm d1;
	d1.tm_year=2000;
	d1.tm_mon=1;
	d1.tm_mday=1;
	date=d1;
}
Concert::Concert(std::string concertName, std::vector<std::string> friendsList, int _desire, std::tm _date){
	//Constructor
	cName=concertName;
	friends=friendsList;
	desire=_desire;
	date=_date;
}

//Less than operator overloading.
//Takes a const reference to the "other" concert.
//returns true if the calling concert is less than the "other"
bool Concert::operator<(const Concert& concert)const{
	//this calls the helper function below
	int dateComp=compareDates(this->getDate() , concert.getDate());
	if(dateComp==0){//if they are equal,
		int desComp= this->desire - concert.getDesire();//compare the desires 
		if(desComp==0){//if equal,
			return false;//They are the same so not less than
		}
		else if(desComp>0)//if this one is higher, not less than
			return false;
		else //it is less than.
			return true;
	}
	else	//else, this one is smaller/
		return true;


}
//This is a helper function to compare two dates.  
//NOTE: THIS IS NOT A PRECISE FUNCTION.
//THERE IS NO ACCOUNTING FOR LEAP YEARS OR DIFFERENCES IN HOW MANY DAYS IN A MONTH.
//It takes the amount of days since jan 1 1970 and returns the difference between the two #s 
int Concert::compareDates(std::tm d1, std::tm d2)const{
	int y1=d1.tm_year -1970;//years since 1970
	int y2=d2.tm_year -1970;
	int year= y1 - y2;//difference in years
	
	int mon = d1.tm_mon - d2.tm_mon;//diff of # of months since Jan.
	
	int day= d1.tm_mday - d2.tm_mday;//diff of # of days since 1st of the month.
	
	int diff;
	diff = year * 365;//difference in years * 365
	diff += mon * 31;//difference in months * 31
	diff += day * 1;//days *1 just for readability.
	return diff;
}
//IGNORE THIS FUNCTION
//0 means equal
//1 means that d1 is greater/later than d2
//-1 means that d2 is greater/later than d1.
int Concert::compareDates2(std::tm d1, std::tm d2)const{

	if(d1.tm_year > d2.tm_year)
		return 1;
	else if(d1.tm_year == d2.tm_year){
		if(d1.tm_mon > d2.tm_mon)
			return 1;
		else if(d1.tm_mon == d2.tm_mon){
			if(d1.tm_mday > d2.tm_mday)
				return 1;
			else if(d1.tm_mday == d2.tm_mday)
				return 0;
			else
				return -1;
		}
		else
			return -1;
	}
	else	
		return -1;
}


//Overriding the stream operator.
//This takes a const reference to a concert and a ostream.
//adds all the text to the stream and returns it.
std::ostream& operator<<(std::ostream& os, const Concert& concert){
	std::tm date=concert.getDate();
	os <<	"\nConcert Name:\t" << concert.getConcertName()  << std::endl;
	os << "Date of Event:\t" << date.tm_mon << "/" << date.tm_mday << "/" << date.tm_year << std::endl;	
	os <<	"List of Friends Attending: " << std::endl;
	for(int i=0;i<concert.getFriends().size();i++){
		os << "\t" << concert.getFriends()[i] << "\n";
	}
	os << "Desire to Attend: " << concert.getDesire() << std::endl;
	return os;
}


//Prints what the stream operator does except straight to std::cout
void Concert::printConcert(){
	std::cout <<	"\nConcert Name: " << cName << std::endl;
	std::cout <<	"List of Freinds Attending: " << std::endl;
	for(int i=0;i<friends.size();i++){
		std::cout << "\t" << friends[i] << "\n";
	}
	std::cout << "Desire to Attend: " << desire << std::endl;
	std::cout << "Date of Event: " << date.tm_mon << "/" << date.tm_mday << "/" << date.tm_year << std::endl;	
}



//Getters

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


//Setters

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
