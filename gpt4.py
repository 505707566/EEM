
import requests

url = 'https://gcraoai5sw1.openai.azure.com/openai/deployments/gpt-4-32k/chat/completions?api-version=2023-03-15-preview'
api_key = '90ae57c5890f4d02bddef7c3cef4634d'  
headers = {'Content-Type': 'application/json', 'api-key': api_key}  
data = {  
    "messages": [  
        {"role": "system", "content": "You are a helpful assistant."},  
        {"role": "user", "content": "What are the 10 most important backgrounds to understand Les Misérables?"},
        {"role": "assistant", "content": "Assistant's Response: 1. French Revolution (1789-1799): It is essential to understand the French Revolution's ideals and radical changes to contextualize the social and political atmosphere in \"Les Misérables.\" The French people revolted against the monarchy, resulting in the rise of Napoleon and the eventual restoration of a constitutional monarchy.2. Bourbon Restoration (1814-1830): Following the fall of Napoleon, the French monarchy was restored with the Bourbon dynasty. Their policies led to widespread dissatisfaction, giving rise to another revolution in 1830.3. July Revolution (1830): This three-day revolt resulted in the fall of the Bourbon monarchy and the ascent of the \"Citizen King\" Louis-Philippe, whose reign fueled the social and political unrest depicted in \"Les Misérables.\"4. June Rebellion (1832): \"Les Misérables\" focuses on this minor but symbolically significant uprising that occurred due to economic hardship, political repression, and rising Republican sentiment. The novel's main battle scene takes place during this rebellion.5. Social Inequality: Les Misérables addresses the extreme social inequality that existed in 19th-century France, with the majority living in poverty and facing harsh working conditions while the monarchy and upper class continued to flourish.6. Urbanization and Industrialization: During the 19th century, France saw rapid industrialization and urban growth, which led to overcrowding, unemployment, and further social disparities.7. Victor Hugo: Hugo was a staunch defender of human rights and social reform. Understanding his motivations and beliefs will help readers appreciate the themes and arguments presented in \"Les Misérables.\"8. Romanticism: Literary Romanticism, a movement that celebrated emotion, imagination, and individualism, heavily influenced \"Les Misérables.\" Hugo was associated with this movement, and its principles are reflected in his portrayal of characters and societal events.9. Catholicism: Religion plays a significant role in \"Les Misérables,\" with characters often grappling with morality, forgiveness, and redemption. Understanding the Catholic belief system and the story of the bishop, who is a pivotal figure in the novel, is essential.10. Literary Themes and Motifs: \"Les Misérables\" covers themes of redemption, morality, justice, love, and sacrifice. Familiarity with these themes will help readers analyze and interpret the novel's intricate narrative and character portrayal."},
        {"role": "user", "content": "Provide me a summary of a random chapter of this book in 10 random languages:"}
    ],  
    "max_tokens": 500,
    "temperature": 0.7,
    "n":3
}

resp = requests.post(url, json=data, headers=headers)


print(resp.json())
