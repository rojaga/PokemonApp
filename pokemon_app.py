import requests

while True:
    
    # Prompt a question
    question = input("What pokemon are you looking for? ")
    
    # Transform input to lowercase for proper api url consumption
    question = question.lower()
    
    # Setting the URL as a variable for ease of use
    url = f"https://pokeapi.co/api/v2/pokemon/{question}"
    
    # This is where the API call happens
    req = requests.get(url)
    
    # Process the code only if a search is valid
    if req.status_code == 200:
        
        # JSON-ify the response
        pokemon = req.json()
        
        # Print some data
        print("Pokemon details:\n")
        print("Name:", pokemon['name'])
        print("Weight:", pokemon['weight'])
        print("Height:", pokemon['height'])
        
        print("Abilities:")
        
        # Get Abilities list
        for ability in pokemon['abilities']:
            print("\tAbility:", ability['ability']['name'])
            
        print("Moves:")
        # Get Moves list
        for move in pokemon['moves']:
            print("\tMove:", move['move']['name'])
        
    else:
        print("Your search is invalid. Please try again.")
        
        