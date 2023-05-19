#  import setup and run from index.py
from index import setup, run
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

setup({"OPENAI_API_KEY": "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",
       "instructions": "The following is a user interview about a product called Stubs. Parse it as a table with the following columns in order: user_job (text | NA), users_pain_points (list | NA), previous_solutions_used (list | None | NA), user_interested_in_product (Yes | No | NA)",
       })

history = []

human = """Thanks

You're welcome! It was great talking to you and learning about your experience as an NFT artist. If you have any other questions or feedback in the future, feel free to reach out. Have a great day!

2023-05-18 06:33:33

/run

That's dope

Yes, it definitely is! Is there anything else you'd like to know about Stubs or any other questions you have?

2023-05-18 06:33:17

/run

Oh that's awesome, how do I sign up

You can sign up for beta invites on the Stubs website. Just go to the website and click on the "Sign up for beta invites" button. From there, you'll be asked to provide your email address and some basic information about yourself. Once you've signed up, you'll be notified when the beta version of Stubs is available and you can start creating, launching, and monetizing your digital assets with ease.

2023-05-18 06:32:55

/run

Would Stubs let me create tokengated pages?

Yes, Stubs allows you to set up tokengated mint pages in minutes. This means that you can create pages where users need to hold a specific token in order to access or mint your digital assets. This can be a great way to incentivize users to hold your token and increase its value.

2023-05-18 06:32:38

/run

Oh awesome

Glad to hear that! Is there anything else you'd like to know about Stubs or any other questions you have?

2023-05-18 06:32:02

/run

Of course

Great! Stubs is a user-friendly platform that guides you step-by-step through the entire process of creating and launching your digital assets. You can create no-code galleries, personal pages, and storefronts, build and publish decentralized blogs effortlessly, set up tokengated mint pages in minutes, integrate payment gateways for seamless monetization, and connect your favorite services, like Shopify, for an enhanced experience. Stubs is designed to empower everyone to create, launch, and monetize in Web3 with ease, while maintaining top-notch quality and reliability. It removes technical jargon and hurdles, so you can focus on your ideas and bring your vision to life. If you're interested in trying out Stubs, you can sign up for beta invites and join the platform to start creating, launching, and monetizing your digital assets with ease.

2023-05-18 06:31:36

/run

Yeah thirdweb, you know it?

I'm not familiar with Thirdweb, but I can tell you about a new product called Stubs. Stubs is a no-code page builder for Web3 that can help you create, launch, and monetize your digital assets with ease. With Stubs, you don't need any technical knowledge to deploy your digital assets. Would you be interested in learning more about Stubs and how it can help you with your NFT art?

2023-05-18 06:31:18

/run

I'm not technical so I get stuck at deplying contracts and stuff

I see. So the technical aspects of deploying contracts can be a challenge for you. Have you tried using any no-code solutions to help with this process?

2023-05-18 06:30:52

/run

I'm an NFT artist

That's awesome! As an NFT artist, what are some of the challenges you've faced when it comes to creating and launching your digital assets?

2023-05-18 06:30:37

/run

Of course

Great! To start off, can you tell me a little bit about your experience with Web3 and creating digital assets? What are some of the pain points you've encountered in the process?

2023-05-18 06:30:28

/run

Good good

That's great to hear! My name is UserInterviewGPT and I'm conducting user interviews about a new product called Stubs. Would you be interested in participating in a quick interview?

2023-05-18 06:30:19

/run

Hey

Hello! How are you doing today?"""
output = run(history=history, message=human)

history.append(HumanMessage(content=human))
history.append(AIMessage(content=output))

print("human", human)
print("output", output)