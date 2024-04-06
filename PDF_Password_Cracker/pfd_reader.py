from concurrent.futures import ThreadPoolExecutor
import PyPDF2, time
from datetime import datetime, timedelta

found = ""


def decode(mob):
    start_timein = time.perf_counter()
    is_found = True
    pdf_path = "file/path"
    current_date = datetime(1950, 1, 1)
    while is_found and current_date < datetime.now():
        formatted_date = current_date.strftime("%d%m%y")
        password = f"{mob:05}" + formatted_date
        current_date = current_date + timedelta(days=1)
        try:
            # Open the PDF file
            with open(pdf_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                # Check if the PDF is encrypted
                if pdf_reader.is_encrypted:
                    # Attempt to decrypt it
                    if pdf_reader.decrypt(password):
                        print(
                            "PDF successfully decrypted. You can now read the content."
                        )
                        is_found = False
                        print(password)
                        print(f"Number of pages: {pdf_reader.pages}")
                        # You can add more code here to read or manipulate the PDF
        except Exception as e:
            print(f"An error occurred: {e}")
    end_timeout = time.perf_counter()
    execution_timeout = end_timeout - start_timein
    print("Execution time for mob series : ", mob, "-->", execution_timeout, " seconds")


start_time = time.perf_counter()
with ThreadPoolExecutor(max_workers=1000) as executor:
    # change the loop variable to suit your mobile number or leave it to try all
    for i in range(11, 100000):
        executor.submit(decode, i)

# Record the end time
end_time = time.perf_counter()

# Calculate and print the execution time
execution_time = end_time - start_time
print(f"Execution time main: {execution_time} seconds")
