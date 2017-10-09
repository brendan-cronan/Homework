#include <vector>
#include <string>
#include <iostream>


class Concert{

	public:
Concert();	
Concert(std::string concertName,std::vector<std::string> friendsList, int _desire, std::tm _date);
//Concert~();
		bool operator<(const Concert& concert)const;
		//std::ostream operator<<(const Concert& c,std::ostream)
		void printConcert();

	
	//Getters
		std::string getConcertName()const;
		std::vector<std::string> getFriends()const;
		int getDesire()const;
		std::tm getDate()const;
		
	//Setters
		void setConcertName(std::string name);
		void setFriend(std::string friendName);
		void setDesire(int _desire);
		void setDate(std::tm _date);
		void setDate(int y,int m,int d);


	private:
		int compareDates(std::tm d1,std::tm d2)const;
		std::string cName;
		std::vector<std::string> friends;	
		int desire;
		std::tm date;
















};
