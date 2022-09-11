class Jar():


    def __init__(self, capacity: int, current_amount: int, desired_amount: int) -> None:   
        """_summary_

        Args:
            capacity (int): _description_
            current_amount (int): _description_
            desired_amount (int): _description_

        Raises:
            Exception: _description_
            Exception: _description_
            Exception: _description_
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
        """"""
        return self.__capacity

    
    @property
    def current_amount(self):
        """"""
        return self.__current_amount


    @property
    def desired_amount(self):
        """"""
        return self.__desired_amount


    @current_amount.setter
    def current_amount(self, new_amount: int) -> None:
        """"""        
        if new_amount > self.__capacity:
            raise Exception
        if isinstance(new_amount, int):
            self.__current_amount = new_amount


    def remove_water(self, amount: int) -> None:
        """_summary_

        Args:
            amount (int): _description_

        Raises:
            Exception: _description_
        """        
        if amount < 0 or amount > self.__current_amount:
            raise Exception

        self.__current_amount -= amount


    def add_water(self, amount: int) -> None:
        """_summary_

        Args:
            amount (int): _description_

        Raises:
            Exception: _description_
        """        
        if amount < 0 or amount + self.__current_amount > self.__capacity:
            raise Exception
        
        self.__current_amount += amount

    
    def full(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """        
        return self.current_amount == self.desired_amount


    def empty(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """        
        return self.current_amount == 0
        

    @staticmethod
    def water_dump(jar_gives, jar_receives):
        """_summary_

        Args:
            jar_gives (_type_): _description_
            jar_receives (_type_): _description_

        Returns:
            _type_: _description_
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
        """_summary_

        Args:
            jar_gives (_type_): _description_
            jar_receives (_type_): _description_

        Returns:
            _type_: _description_
        """        
        if jar_gives.empty() or jar_receives.full():
            return False
        
        return True
