import requests
from dotenv import load_dotenv
load_dotenv()

import base64
import json
import os

wp_user ='raqib'
wp_pass ='YmG2 FFXa 3niv 3gpu CBlo ksHT'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

import openai
openai.api_key = os.getenv("API")

file = open("keyword.txt", "w",)
file.writelines(input("write something"))
file.close()


file = open("keyword.txt", "r")
data = file.readline()
file.close()


"""
      This wil open ai function
  """
def opeai_ans(comand):
 response = openai.Completion.create(
   model="text-davinci-003",
   prompt= (comand + data ) ,
   temperature=0.7,
   max_tokens=256,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0
  )
 output = response.get("choices")[0].get("text")
 return output

"""
      This wil Wordpress function
  """
intro = opeai_ans( f"write a short intro under 100 word about")
def wp_paragraph(text):
    codes = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return codes

wp_intro= wp_paragraph(intro)

photo_1 = "https://cdn.shopify.com/s/files/1/1109/6048/products/media_ef752dcf-fb80-40fe-8a00-21df1474c3f4_large.png?v=1655774218"
def photo(img_src,title):
    codes = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} -->' \
            f'<figure class="wp-block-image aligncenter size-large">' \
            f'<img src="{img_src}" alt="{title} image"/>' \
            f'<figcaption>{title}</figcaption></figure>' \
            f'<!-- /wp:image -->'
    return codes


title = opeai_ans("write a blog title")
wp_photo1 = photo(photo_1, title)


hh2 = ("Lear more About"+data)
def wp_heading_two(xxx ):
    return f'<!-- wp:heading --><h2>{xxx}</h2><!-- /wp:heading -->'
h2 = wp_heading_two(hh2)

details = opeai_ans( "write buying guide about ")
wp_details = wp_paragraph(details)


content = wp_intro, wp_photo1, h2, wp_details

print(content)

def slugify(title):
    code = title.strip().replace(' ','-')
    return code
slug = slugify

wp_post_url = 'https://localhost/testsite/wp-json/wp/v2/posts'
data = {
    'title': title,
    'content': content,
    'slug': slug,
}

res = requests.post(wp_post_url, data=data, headers=wp_headers, verify=False)
