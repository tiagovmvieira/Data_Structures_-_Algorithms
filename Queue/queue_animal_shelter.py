from termcolor import colored

# Implement a cat and dog queue for an animal shelter

class AnimalShelter:
    def __init__(self):
        self.list_of_dogs = []
        self.list_of_cats = []
        self.list_of_animals = []

    def __str__(self)-> str:
        animals = [str(animal) for animal in self.list_of_animals] if self.list_of_animals else None
        dogs = [str(dog) for dog in self.list_of_dogs] if self.list_of_dogs else None
        cats = [str(cat) for cat in self.list_of_cats] if self.list_of_cats else None  
        
        list_of_animals = ' '.join(animals) if animals else str(animals)
        list_of_dogs = ' '.join(dogs) if dogs else str(dogs)
        list_of_cats = ' '.join(cats) if cats else str(cats)

        return "Animal's Queue: {}, Dog's Queue: {}, Cat's Queue: {}".format(list_of_animals, list_of_dogs, list_of_cats)

    def is_empty(self, type: str = 'Animal')-> bool:
        if type == 'Cat':
            if len(self.list_of_cats) == 0:
                return True
            return False
        elif type == 'Dog':
            if len(self.list_of_dogs) == 0:
                return True
            return False
        elif type == 'Animal':
            if len(self.list_of_animals) == 0:
                return True
            return False
        else:
            return 'Shelter can only accept Dogs or Cats'

    def enqueue(self, animal: str, type: str)-> str:
        if type == 'Cat':
            self.list_of_cats.append(animal)
            self.list_of_animals.append(animal)
        elif type == 'Dog':
            self.list_of_dogs.append(animal)
            self.list_of_animals.append(animal)
        else:
            return 'Shelter can only accept Dogs or Cats'
        return 'The animal is inserted at the end of the Queue'

    def dequeue_cat(self)-> str:
        if self.is_empty('Cat'):
            return 'There is not any Cat in the Queue'
        return self.list_of_cats.pop(0)

    def dequeue_dog(self)-> str:
        if self.is_empty('Dog'):
            return 'There is not any Dog in the Queue'
        return self.list_of_dogs.pop(0)

    def dequeue_any(self)-> str:
        if self.is_empty('Dog') and self.is_empty('Cat'):
            return 'There is not any animal in the Queue'
        return self.list_of_animals.pop(0)

    def peek(self, type: str = 'Animal')-> str:
        if self.is_empty(type):
            return 'There is not any {} in the Queue'.format(type)

        if type == 'Cat':
            return self.list_of_cats[0]
        elif type == 'Dog':
            return self.list_of_dogs[0]
        elif type == 'Animal':
            return self.list_of_animals[0]
        else:
            return 'Shelter can only accept Dogs or Cats'

if __name__ == '__main__':
    print(colored('------------------ QUEUE ANIMAL SHELTER ------------------', 'red'))
    animal_shelter = AnimalShelter()
    print(animal_shelter)

    print(colored('----------------- CHECK IF QUEUE IS EMPTY ----------------', 'red'))
    print('Is animal shelter empty?', animal_shelter.is_empty())
    print("Is dog's queue empty?", animal_shelter.is_empty('Dog'))
    print("Is cat's queue empty?", animal_shelter.is_empty('Cat'))

    print(colored("--------------------- ENQUEUE ANIMALS --------------------", 'red'))
    animal_shelter.enqueue('Cat1', 'Cat')
    animal_shelter.enqueue('Cat2', 'Cat')
    animal_shelter.enqueue('Dog1', 'Dog')
    animal_shelter.enqueue('Cat3', 'Cat')
    animal_shelter.enqueue('Dog2', 'Dog')
    print(animal_shelter)

    print(colored("--------------------- DEQUEUE ANIMALS --------------------", 'red'))
    print(animal_shelter.dequeue_any())
    print(animal_shelter.dequeue_dog())
    print(animal_shelter.dequeue_cat())
    print(animal_shelter.dequeue_any())
    print(animal_shelter)