class Jar():


    def __init__(self, capacity: int, current_amount: int, desired_amount: int) -> None:  
        """Initializes the jar object

        Args:
            capacity (int): maximum amount of water it can take
            current_amount (int): amount of water it starts with
            desired_amount (int): amount of water it needs to have

        Raises:
            Exception: can't have negative or above 40 liters of water
            Exception: can't initiate with more water than it can take
            Exception: can't require more water that it can take
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
        """Removes water from a jar

        Args:
            amount (int): amount of water that will be removed

        Raises:
            Exception: can remove negative water or more water then it has
        """        
        if amount < 0 or amount > self.__current_amount:
            raise Exception

        self.__current_amount -= amount


    def add_water(self, amount: int) -> None:
        """Adds water to a jar

        Args:
            amount (int): amount of water that will be added

        Raises:
            Exception: can't add negative water or surpass the capacity of the jar
        """        
        if amount < 0 or amount + self.__current_amount > self.__capacity:
            raise Exception
        
        self.__current_amount += amount

    
    def full(self) -> bool:    
        """Checks if a jar is full a water

        Returns:
            bool: True is current amount equals to capacity
        """        
        return self.current_amount == self.capacity


    def empty(self) -> bool:   
        """Checks if a jar is empty

        Returns:
            bool: True if current amount is 0
        """        
        return self.current_amount == 0
        

    @staticmethod
    def water_dump(jar_gives, jar_receives):
        """Puts water from a jar to another 

        Args:
            jar_gives (Jar): jar that will give the water
            jar_receives (Jar): jar that will receive the water

        Returns:
            Jar: both jars with new amounts of water
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
        """Checks if it's possible to perform water dump from a jar to another

        Args:
            jar_gives (Jar): jar that will give the water
            jar_receives (Jar): jar that will receive the water

        Returns:
            bool: True if it's possible to perform water dump between jars
        """        
        if jar_gives.empty() or jar_receives.full():
            return False
        
        return True
