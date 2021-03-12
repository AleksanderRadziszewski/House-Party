![Zrzut ekranu 2021-02-25 o 19 30 46](https://user-images.githubusercontent.com/56914063/109521785-f5ff1d00-7aad-11eb-9c70-14ec761f9713.png)
# House-Party

This project will be updated consistently. I want to combine Django, Django Rest Framework and React.js

# 1. Room objects
## a) List of rooms (DRF-JSON document)

![Zrzut ekranu 2021-02-20 o 18 41 45](https://user-images.githubusercontent.com/56914063/108603999-8ac99280-73ab-11eb-99f1-b435677095ad.png)

 ## b) Automatically filled code, host, create at fields. Create Room

![Zrzut ekranu 2021-02-25 o 19 30 46](https://user-images.githubusercontent.com/56914063/109522626-c3095900-7aae-11eb-883c-9e1cfd86f29c.png)

## c) Guest form

![Zrzut ekranu 2021-03-2 o 13 15 44](https://user-images.githubusercontent.com/56914063/109647453-98280f00-7b59-11eb-90b9-7709f4630a55.png)

# 2. Form functionalities 

## a) Handlers - guest can pause change and votes change

![Zrzut ekranu 2021-03-3 o 13 13 20](https://user-images.githubusercontent.com/56914063/109820553-66847600-7c35-11eb-8f99-bfb754067765.png)

## b) Creating Room object by form

![Zrzut ekranu 2021-03-4 o 14 41 14](https://user-images.githubusercontent.com/56914063/109973151-55e90400-7cf8-11eb-90f7-11c23125b6e1.png)

## c) Calling API endpoints from React

### 1. Correct request

![Zrzut ekranu 2021-03-8 o 14 15 14](https://user-images.githubusercontent.com/56914063/110327731-a32be500-801a-11eb-8c02-11c036d39bb1.png)

### 2. Bad request, invalid Room code parameter

![Zrzut ekranu 2021-03-7 o 12 52 17](https://user-images.githubusercontent.com/56914063/110238855-1e6e9780-7f44-11eb-9fe4-abfe4d09fbd7.png)

### 3. Bad request, Room code parameter not found in request

![Zrzut ekranu 2021-03-7 o 12 58 05](https://user-images.githubusercontent.com/56914063/110238973-c8e6ba80-7f44-11eb-9a81-7080faa6380a.png)

### 4. Request ok, Room code parameter exist and is founded

I pick the first one

![Zrzut ekranu 2021-03-7 o 12 59 25](https://user-images.githubusercontent.com/56914063/110239037-2da21500-7f45-11eb-9e43-ed90bb085599.png)

Result, is_host = False

![Zrzut ekranu 2021-03-7 o 13 07 31](https://user-images.githubusercontent.com/56914063/110239217-27f8ff00-7f46-11eb-80d4-ee6bbfb25436.png)

Result, is_host = True

![Zrzut ekranu 2021-03-7 o 13 12 12](https://user-images.githubusercontent.com/56914063/110239360-d604a900-7f46-11eb-84c3-8281f3481be3.png)

We take room with code KFFJXZ and change some settings.

![Zrzut ekranu 2021-03-8 o 14 32 00](https://user-images.githubusercontent.com/56914063/110328285-74623e80-801b-11eb-8187-a166edc7c623.png)

After pushing the button "Create room"

![Zrzut ekranu 2021-03-8 o 14 32 10](https://user-images.githubusercontent.com/56914063/110328309-7c21e300-801b-11eb-91a9-7838ab0dce56.png)
 

 ## d) Join Room Panel

### 1. Before focus 

 ![Zrzut ekranu 2021-03-10 o 14 19 59](https://user-images.githubusercontent.com/56914063/110636191-43654380-81ac-11eb-9799-7f7075092e83.png)

### 2. After focus

![Zrzut ekranu 2021-03-10 o 14 20 08](https://user-images.githubusercontent.com/56914063/110636250-56781380-81ac-11eb-8536-8c9bc9e96a78.png)






