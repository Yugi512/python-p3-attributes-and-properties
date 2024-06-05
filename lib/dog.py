#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self,name = "Dog",breed ="Breed"):
        self.name = name
        self.breed = breed

    def get_name(self):
        print("getting name")
        return self._name
    
    def get_breed(self):
        print("getting breed")
        return self._breed

    def set_name(self,name):
        if (type(name) == str) and (0 < len(name) <= 25 ): 
            self._name = name
        else: 
            print("Name must be string between 1 and 25 characters.")
    
    def set_breed(self,breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        if breed in APPROVED_BREEDS:
            self._breed = breed
        
    breed = property(get_breed,set_breed)
    name = property(get_name,set_name)
