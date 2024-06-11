class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    
    def create_recipe(self):
        al=self.ingredients.split(',')
        with open(f'{self.name}.txt','a') as f:
            f.write(f'Recipe: {self.name}\n')
            for i in al:
                f.write(f'Ingredients: {i}\n')
            f.write(f'Instructions: {self.instructions}\n')
        with open(f'{self.name}.txt','r') as f:
            print(f.read())

    def search(self):
        with open(f'{self.name}.txt','r') as f:
            print(f.read())
            print('--------------------------------------------------')
            print()
try:
    x=1
    recipes=[]
    recipe_num=[]
    while x>=1:
        print('1. Create a recipe')
        print('2. Search a recipe')
        print('3. Exit')
        ch=[1,2,3]
        chc=int(input('Enter your choice: '))    
        if chc in ch:
            if chc==1:
                name=input('Enter the name of the recipe: ')
                ingredients=input('Enter the ingredients: ')
                instructions=input('Enter the instructions: ')
                recipe=Recipe(name,ingredients,instructions)
                recipe.create_recipe()
                recipes.append(recipe)
                recipe_num.append(name)
            elif chc==2:
                name=input('Enter the name of the recipe: ')
                if name in recipe_num:
                    for i in recipes:
                        if i.name==name:
                            i.search()
                        else:
                            print('Recipe not found')
            elif chc==3:
                print("Thank you")
                break
        else:
            print('Invalid choice')
except(TypeError,ValueError,IndexError):
    print("Invalid input")