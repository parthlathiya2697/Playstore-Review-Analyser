import openai

# Custom
from utils.private import Creds

# Globals
openai.api_key = Creds.OPENAI_API_KEY


def text_limitor(func):
    
    def inner1(*args, **kwargs):
         
        max_words= 3000  # based on max_token_limit= 4000
        text = args[0]
        text = '. '.join(text.split(' ')[: max_words])
        text = text.replace('"', '\'')  # complement to the use of fstring
         
        # getting the returned value
        returned_value = func(text, **kwargs)
         
        # returning the value to the original frame
        return returned_value
         
    return inner1


@text_limitor
def points_of_improvements(text: str):
    
    # TODO: Update
    # brute force text shrink
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"List out all the Points of Improvements that can be analysed from the Product User's Reviews\nInput: Product User's Reviews\nOutput: Points of Improvements\n\n###-###\n\nProduct User's Reviews:\n{text}"},
            {"role": "user", "content": ""},
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    response = response.choices[0].message.content
    return response


@text_limitor
def paraphrase(text: str):
  response = openai.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=[
                  {"role": "system", "content": f"Paraphrase/Rewrite the Original Text without any Plagiarism or loss and addition of information\n\n---\n\nOriginal: Her life spanned years of incredible change for women as they gained more rights than ever before.\n\nParaphrase: She lived through the exciting era of women's liberation.\n\nOriginal: Giraffes like Acacia leaves and hay, and they can consume 75 pounds of food a day.\n\nParaphrase: A giraffe can eat up to 75 pounds of Acacia leaves and hay daily.\n\nOriginal: Any trip to Italy should include a visit to Tuscany to sample the region's exquisite wines.\n\nParaphrase: Be sure to make time for a Tuscan wine-tasting experience when visiting Italy.\n\nOriginal: Symptoms of influenza include fever and nasal congestion.\n\nParaphrase: A stuffy nose and elevated temperature are signs you may have the flu.\n\nOriginal: The price of a resort vacation typically includes meals, tips and equipment rentals, which makes your trip more cost-effective.\n\nParaphrase: All-inclusive resort vacations can make for an economical trip.\n\nOriginal: He has tons of stuff to throw away.\n\nParaphrase: He needs to get rid of a lot of junk.\n\nOriginal passage:\n\nIn The Sopranos, the mob is besieged as much by inner infidelity as it is by the federal government. Early in the series, the greatest threat to Tony's Family is his own biological family. One of his closest associates turns witness for the FBI, his mother colludes with his uncle to contract a hit on Tony, and his kids click through Web sites that track the federal crackdown in Tony's gangland.\n\nParaphrased passage:\n\nIn the first season of The Sopranos, Tony Soprano’s mobster activities are more threatened by members of his biological family than by agents of the federal government. This familial betrayal is multi-pronged. Tony’s closest friend and associate is an FBI informant, his mother and uncle are conspiring to have him killed, and his children are surfing the Web for information about his activities.\n\n---\n\nOriginal passage:\n\n{text}\n\nPrarphrased passage:"},
                  {"role": "user", "content": ""},
              ],
              max_tokens=1000,
              temperature=0.7,
          )
  response = response.choices[0].message.content
  return response


@text_limitor
def emojify(text: str):
  
  response = openai.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=[
                  {"role": "system", "content": f"Insert relevant Emojis according to the mood of the language  in the text and format the text with better spacings:\n-----\nText:\nCan someone have a good attitude and still not like their job?\nYes, it is possible to have a positive mindset and still dislike your job. Regardless of their employment circumstances, a person's attitude relates to their general perspective and manner. It can be either good or negative. For instance, even if someone has a positive outlook and tries to see the bright side of things, they may still not love their work because of things like a challenging workplace, a lack of fulfilment or purpose in their work, or a lack of prospects for progress. On the other side, someone may have a bad attitude while liking their job because of problems or obstacles in their personal life that have nothing to do with their profession. In general, having a positive outlook can make you more resilient and driven, but it's also critical to pay attention to your overall job happiness and make changes as needed to find employment that is satisfying and meaningful to you.\n\nText emojis:\nCan someone have a good attitude and still not like their job?\nYes, it is possible to have a 🤩 positive mindset and still dislike your job. Regardless of their employment circumstances, a person's attitude relates to their general perspective and manner. It can be either good or negative. For instance, even if someone has a positive outlook and tries to see the bright side of things, they may still not love their work because of things like a challenging workplace, a lack of fulfilment or purpose in their work, or a lack of prospects for progress. On the other side, someone may have a 🤨 bad attitude while liking their job because of problems or obstacles in their personal life that have nothing to do with their profession. In general, having a 🤗 positive outlook can make you more resilient and driven, but it's also critical to pay 💭 attention to your overall job happiness and make changes as needed to find employment that is satisfying and meaningful to you.\n-----\nText:\n{text}\n\nText emojis:"},
                  {"role": "user", "content": ""},
              ],
              max_tokens=2355,
              temperature=0.71,
          )
  response = response.choices[0].message.content
  return response