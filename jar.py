class Jar():


    def __init__(self, capacity: int, current_amount: int, desired_amount: int) -> None:  
        """Initializes a Jar object

        Args:
            capacity (int): Amount of water the jar can take
            current_amount (int): Amount of water the jar currently has
            desired_amount (int): Amount of water the jar needs to end up with

        Raises:
            Exception: Capacity can't be negative or above 40
            Exception: Jar can't have negative water or more water than it can take
            Exception: Jar can't need negative water or more water than it can't take
        """                   
        if capacity > 40 or capacity < 0:
            raise Exception
        elif current_amount > capacity or current_amount < 0:
            raise Exception
        elif desired_amount > capacity or desired_amount < 0:
            raise Exception

        self.__capacity = capacity
        self.__current_amount = current_amount
        self.__desired_amount = desired_amount


    @property
    def capacity(self):
        """Capacity getter"""
        return self.__capacity

    
    @property
    def current_amount(self):
        """Current amount getter"""
        return self.__current_amount


    @property
    def desired_amount(self):
        """Desired amount getter"""
        return self.__desired_amount


    @current_amount.setter
    def current_amount(self, new_amount: int) -> None:
        """Current amount setter"""
        if new_amount > self.__capacity:
            raise Exception
        if isinstance(new_amount, int):
            self.__current_amount = new_amount


    def remove_water(self, amount: int) -> None:  
        """Removes an amount water from a jar by subtracting this amount from the 
           current_amount.

        Args:
            amount (int): Amount of water that will be removed from the jar

        Raises:
            Exception: Can't remove negative water or remove more than the jar has
        """        
        if amount < 0 or amount > self.__current_amount:
            raise Exception

        self.__current_amount -= amount


    def add_water(self, amount: int) -> None:      
        """Adds an certain amount of water in a jar by adding this amount 
           to the current_amount.

        Args:
            amount (int): Amount of wataer that will be added to the jar

        Raises:
            Exception: Can't add negative water or surpass the jar's capacity
        """        
        if amount < 0 or amount + self.__current_amount > self.__capacity:
            raise Exception
        
        self.__current_amount += amount

    
    def full(self) -> bool: 
        """Checks if a jar is full of water by comparing the current_amount 
           with the capacity

        Returns:
            bool: True if the jar is full else False
        """                 
        return self.current_amount == self.capacity


    def empty(self) -> bool:         
        """Checks if a jar is empty by looking at the current amount

        Returns:
            bool: True of jar has no water False otherwise
        """
        return self.current_amount == 0
        

    @staticmethod
    def water_dump(jar_gives, jar_receives):   
        """Dumps water from a jar to another jar. Dumps all the water from the jar_gives into
           the jar_receives or fills up the jar_receives. 

        Args:
            jar_gives (Jar): Jar that will lose water
            jar_receives (Jar): Jar the will receive water

        Returns:
            Jar: returns the two jar objects with the new amount of water after the dump
        """        
        jar_receives_remaining_capacity = jar_receives.capacity - jar_receives.current_amount

        if (jar_gives.current_amount == jar_receives_remaining_capacity) or (jar_gives.current_amount < jar_receives_remaining_capacity):
            jar_receives.add_water(jar_gives.current_amount)
            jar_gives.remove_water(jar_gives.current_amount)
        else:
            jar_receives.add_water(jar_receives_remaining_capacity)
            jar_gives.remove_water(jar_receives_remaining_capacity)

        return jar_gives, jar_receives


    @staticmethod
    def check_water_dump_possibility(jar_gives, jar_receives): 
        """Checks if it's possible to do a water dump between two jars. It's not
           possible when the jar that gives is empty or the jar that receives is 
           full.

        Args:
            jar_gives (Jar): Jar that gives water (can't be empty)
            jar_receives (Jar): Jar that receives water (can't be full)

        Returns:
            bool: True if the water dump is possible False otherwise
        """             
        if jar_gives.empty() or jar_receives.full():
            return False
        
        return True
