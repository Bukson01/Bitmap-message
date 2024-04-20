import sys

def display_bitmap_message(bitmap):
    print('Bitmap Message')
    message = input('Enter the message to display with the bitmap: ').strip()
    
    if not message:
        print("Message cannot be empty. Exiting.")
        sys.exit()

    # Print the bitmap message
    [print(''.join(message[i % len(message)] if bit != ' ' else ' ' for i, bit in enumerate(line))) for line in bitmap.splitlines()]

# Example bitmap
bitmap = """
                *********                    
             ***************                 
           *******************               
          ********************              
         ***********************             
        ************************            
        *************************           
        **************************          
        ***************************         
        ****************************        
         ****************************      
          *****************************     
           *****************************   
            *****************************  
             ***************************** 
              ****************************
               ***************************
                 *************************
                   ***********************
                     *********************
                       *****************
                          *************
                            *********
                              *****
                                *
"""

# Display the bitmap message
display_bitmap_message(bitmap)
