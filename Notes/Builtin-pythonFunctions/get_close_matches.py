from difflib import get_close_matches


def check_topics(user_input) -> str:
    
    topics_dict:dict[str:str] = {
        'topics':('btc','weather','music','weather','date'),        
        }
    topic_matches:list[str] = [v for v in topics_dict['topics']]
    Topics:list[str] = get_close_matches(user_input, topic_matches, n=2, cutoff=0.6)
    
    if Topics:
        return Topics[0]
    else:
        return f'No items that match'

def main():
    user_input = input('Topic ')
    output_found:str = check_topics(user_input) 
    print(f'{output_found}')
 
if __name__ == "__main__":
    main()
 