import os
""""
WAAAAAAAAAAAAAAAAAAAAH I don't know this part, so I use AI to generate it for me. I hope it works, 
if not, then :>.

"""
def take_screenshot(page, test_number, image_name):
    """
    Saves a screenshot in a numbered folder with a custom filename.
    Example: test_evidence/Test_1/Login_Success.png
    """
    # 1. Create the numbered folder (e.g., Test_1, Test_2)
    base_folder = "test_evidence"
    test_folder = os.path.join(base_folder, f"Test_{test_number}")
    
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    
    # 2. Use your custom image name
    # We ensure it ends with .png
    if not image_name.endswith(".png"):
        image_name += ".png"
        
    filepath = os.path.join(test_folder, image_name)
    
    # 3. Take the shot
    page.screenshot(path=filepath, full_page=True)
    print(f"📸 Evidence saved: {filepath}")
    return filepath