# ������������ �������������:
# import asyncio
# from time import sleep #������� ����� ���������������� ������ ����
# from asyncio import sleep


# def download_photo(photo_count, limit):
#     while True:
#         if photo_count > limit:
#             break
#         sleep(1) #��������� ��������:sleep
#         photo_count += 1
#         print(f"Photo {photo_count}...")
#
# def main():
#     photo_count = 0
#     download_photo(photo_count,10)
#
# main()


#
# async def download_photo(photo_count, limit):
#     while True:
#         if photo_count > limit:
#             break
#         await sleep(1) #��������� ��������:sleep
#         photo_count += 1
#         print(f"Photo {photo_count}...")
#
#
# async def download_video(video_count, limit):
#     while True:
#         if video_count > limit:
#             break
#         await sleep(5)
#         video_count += 1
#         print(f"VIDEO {video_count}...")
#
#
# async def main():
#     photo_count = 0
#     video_count = 0
#     task_list = [
#         download_photo(photo_count, 10),
#         download_video(video_count, 5)
#     ]
#     await asyncio.gather(*task_list)
#
#
# asyncio.run(main())