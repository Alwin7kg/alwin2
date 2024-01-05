
<!-- index.html -->
<!DOCTYPE html> 
<html lang="en"> 
  
<head> 
    <meta charset="UTF-8"> 
    <meta name="viewport" 
          content="width=device-width, 
                   initial-scale=1.0"> 
    <link rel="stylesheet" 
          href="style.css"> 
</head> 
  
<body> 
    <div class="outer-box utility_flex"> 
        <div class="box"> 
            <div class="inner-box utility_flex"> 
                <div class="gfglogo utility_flex"> 
                    <h1 class="logo-text"> 
                        GeeksforGeeks 
                    </h1> 
                    <p class="sub-heading"> 
                        Prime Number Finder 
                    </p> 
                </div> 
  
                <div class="input-container"> 
  
                    <input type="number" 
                           class="input-feild" 
                           id="input-id"
                           placeholder= 
                           "Enter the number you want to check"> 
                </div> 
  
                <div class="btn-container utility_flex "> 
                    <button class="btn-clear btn-style" 
                            id="id-clear"> 
                        Clear 
                    </button> 
                    <button class="btn-submit btn-style"
                            id="sub-id"> 
                        Submit 
                    </button> 
                </div> 
  
            </div> 
            <div class="para-text"> 
                <p class="message"
                   id="dom-msg"> 
                  Result 
                  </p> 
            </div> 
        </div> 