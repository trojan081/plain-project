<template>
    <section id="sbsr-298">
        <div class="cs-container">
            <div class="cs-image-group">
                <div class="cs-box">
                    <span class="cs-number">CAD</span>
                    <picture class="cs-box-picture">
                        <source media="(max-width: 600px)" srcset="/public/assets/laptop_cad.jpg">
                        <source media="(min-width: 601px)" srcset="/public/assets/laptop_cad.jpg">
                        <img loading="lazy" decoding="async" src="/public/assets/laptop_cad.jpg" alt="laptop with CAD software" width="521" height="672" aria-hidden="true">
                    </picture>
                </div>
                <picture class="cs-picture">
                    <img loading="lazy" decoding="async" src="/public/assets/laptop_cad.jpg" alt="laptop with CAD software" width="521" height="672" aria-hidden="true">
                </picture>
            </div>
            <div class="cs-content">
                <span class="cs-topper">Комфортная адаптация</span>
                <h2 class="cs-title">Почему Plain - это удобно</h2>
                <p class="cs-text">
                    Используй привычное ПО для проектирования: <br>Plain совместим <strong>с любыми CAD-системами.</strong>
                </p>
                <!-- <p class="cs-text">Если возникли вопросы: support@plain-project.ru</p> -->
            </div>
        </div>
    </section>
</template>

<style scoped>

/* Mobile - 360px */
@media only screen and (min-width: 0rem) {
    #sbsr-298 {
        padding: var(--sectionPadding);
        margin-top: 22%;
    }
    #sbsr-298 .cs-container {
        width: 100%;
        /* changes to 1280px at desktop */
        max-width: 34.375rem;
        margin: auto;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        /* NEW: White background and rounded corners for the container */
        background-color: white;
        border-radius: 50px; /* Adjust for more or less oval shape */
        padding: 2rem; /* Add padding so content doesn't stick to the edges */
        box-shadow: 0px 1px 10px rgba(73, 9, 9, 0.63);
    }
    #sbsr-298 .cs-content {
        /* set text align to left if content needs to be left aligned */
        text-align: center;
        width: 100%;
        max-width: 32.625rem;
        display: flex;
        flex-direction: column;
        /* centers content horizontally, set to flex-start to left align */
        align-items: center;
    }

    #sbsr-298 .cs-text {
        margin-bottom: 1rem;
    }
    #sbsr-298 .cs-text:last-of-type {
        margin-bottom: 2rem;
    }
    #sbsr-298 .cs-link {
        font-size: 1rem;
        font-weight: 700;
        text-decoration: none;
        color: var(--primary);
    }
    #sbsr-298 .cs-button-solid {
        font-size: 1rem;
        /* 46px - 56px */
        line-height: clamp(2.875rem, 5.5vw, 3.5rem);
        text-decoration: none;
        font-weight: 700;
        text-align: center;
        margin: 0;
        color: #fff;
        min-width: 9.375rem;
        padding: 0 1.5rem;
        background-color: var(--primary);
        border-radius: 0.25rem;
        display: inline-block;
        position: relative;
        z-index: 1;
        /* prevents padding from adding to the width */
        box-sizing: border-box;
    }

    #sbsr-298 .cs-image-group {
        width: 100%;
        max-width: 34.375rem;
        /* 78px - 108px */
        margin: 0 auto clamp(4.875rem, 16.5vw, 6.75rem);
        position: relative;
        display: block;
        /* width divided by height */
        aspect-ratio: 0.90358127;
    }
    #sbsr-298 .cs-picture {
        /* big background image */
        width: 80%;
        height: 61%;
        position: absolute;
        top: 0;
        left: 0;
        display: block;
    }
    #sbsr-298 .cs-picture img {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        border-radius: 0.625rem;
        object-fit: cover;
        /* NEW: Move image higher */
        object-position: 50% -10%; /* Adjust as needed */
    }
    #sbsr-298 .cs-box {
        /* NEW: Smaller size for the CAD box */
        width: clamp(8rem, 30vw, 15rem); /* Adjusted values for smaller size */
        height: clamp(8rem, 30vw, 15rem); /* Adjusted values for smaller size */
        border-radius: 0.625rem;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        position: absolute;
        left: 50%;
        /* 38px - 60px - wrapped in a calc function to make clamp values negative */
        bottom: calc(clamp(2.375rem, 7.9vw, 3.75rem) * -1);
        transform: translateX(-50%);
        z-index: 10;
    }
    #sbsr-298 .cs-box-picture {
        /* Background image for cs-box */
        width: 100%;
        height: 100%;
        /* background-color: #e4d7d788; */
        border-radius: 0.625rem;
        /* clips img corners and bg corners */
        overflow: hidden;
        position: absolute;
        top: 0;
        left: 0;
        display: block;
        z-index: -1;
    }
    #sbsr-298 .cs-box-picture img {
        position: absolute;
        top: 0;
        left: 0;
        opacity: 0.65;
        height: 100%;
        width: 100%;
        object-fit: cover;
    }
    #sbsr-298 .cs-number {
        /* 75px - 100px */
        font-size: clamp(4.6875rem, 8vw, 6.25rem);
        line-height: 1em;
        font-weight: 900;
        margin-bottom: 0.5rem;
        color: var(--headerColor);
        /* creates the transparent clipping text */
        mix-blend-mode: screen;
        display: block;
        z-index: 10;
    }
    #sbsr-298 .cs-number:before {
        content: "";
        width: clamp(11.5rem, 45vw, 18.375rem);
        height: clamp(11.5rem, 45vw, 18.375rem);
        opacity: 1;
        background-color: #fffffffa;
        border-radius: 0.4375rem;
        position: absolute;
        display: block;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: -1;
    }
    #sbsr-298 .cs-desc {
        font-size: clamp(1rem, 4vw, 1.5625rem);
        font-weight: 700;
        line-height: 1.2em;
        text-transform: lowercase;
        text-align: center;
        width: 80%;
        color: var(--headerColor);
        position: relative;
        z-index: 10;
    }
}
/* Desktop - 1024px */
@media only screen and (min-width: 64rem) {
    #sbsr-298 {
        /* aligns the button */
        text-align: left;
        opacity: 0.8;
    }
    #sbsr-298 .cs-container {
        max-width: 80rem;
        /* set to horizontal arrangement */
        flex-direction: row;
        justify-content: space-between;
        gap: 10rem;
        /* NEW: White background and rounded corners for desktop container */
        background-color: white;
        border-radius: 50px;
        padding: 3rem; /* Adjust padding for desktop */
    }
    #sbsr-298 .cs-content {
        text-align: left;
        align-items: flex-start;
    }
    #sbsr-298 .cs-image-group {
        width: 40vw;
        max-width: 32.5625rem;
        /* 520px - 672px */
        height: clamp(32.5rem, 51.9vw, 42rem);
        margin: 0;
        /* sends it to the right in the 2nd position */
        order: 2;
    }
    #sbsr-298 .cs-box {
        /* NEW: Smaller size for the CAD box on desktop */
        width: clamp(10rem, 18vw, 15rem); /* Adjusted values */
        height: clamp(10rem, 18vw, 15rem); /* Adjusted values */
        left: auto;
        transform: none;
        /* -52px to -102px */
        left: calc(clamp(3.25rem, 5.5vw + 1.6rem, 6.375rem) * -1);
        /* 62px - 80px */
        bottom: clamp(3.875rem, 6.2vw, 5rem);
    }
    #sbsr-298 .cs-number:before {
        /* 226px - 293px */
        width: clamp(14.125rem, 22.7vw, 18.3125rem);
        height: clamp(14.125rem, 22.7vw, 18.3125rem);
    }
}

:root {
    /* Add these styles to your global stylesheet, which is used across all site pages. You only need to do this once. All elements in the library derive their variables and base styles from this central sheet, simplifying site-wide edits. For instance, if you want to modify how your h2's appear across the site, you just update it once in the global styles, and the changes apply everywhere. */
    --primary: #ff6a3e;
    --primaryLight: #ffba43;
    --secondary: #ffba43;
    --secondaryLight: #ffba43;
    --headerColor: #1a1a1a;
    --bodyTextColor: #4e4b66;
    --bodyTextColorWhite: #fafbfc;
    /* 13px - 16px */
    --topperFontSize: clamp(0.8125rem, 1.6vw, 1rem);
    /* 31px - 49px */
    --headerFontSize: clamp(1.9375rem, 3.9vw, 3.0625rem);
    --bodyFontSize: 1rem;
    /* 60px - 100px top and bottom */
    --sectionPadding: clamp(3.75rem, 7.82vw, 6.25rem) 1rem;
}

body {
    margin: 0;
    padding: 0;
}

*, *:before, *:after {
    /* prevents padding from affecting height and width */
    box-sizing: border-box;
}
.cs-topper {
    font-size: 1.5vw;
    line-height: 5.2em;
    text-transform: uppercase;
    text-align: inherit;
    letter-spacing: .1em;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 0.25rem;
    display: block;
}

.cs-title {
    font-size: 1.3vw;
    font-weight: 900;
    line-height: 3.2em;
    text-align: inherit;
    max-width: 43.75rem;
    margin: 0 0 0 0;
    color: #000000af; /* Existing white text color */
    position: relative;
    /* NEW: White outline for the title text */
    text-shadow:
        -1px -1px 0 #fff,
        1px -1px 0 #fff,
        -1px 1px 0 #fff,
        1px 1px 0 #fff;
}

.cs-text {
    font-size: var(--bodyFontSize);
    line-height: 1.5em;
    text-align: inherit;
    width: 100%;
    max-width: 40.625rem;
    margin: 0;
    color: var(--bodyTextColor);
}
#sbsr-298 {
    padding: var(--sectionPadding);
    margin-top: 15%; /* было 22%, уменьшили */
}

#sbsr-298 .cs-image-group {
    max-width: 28rem; 
    aspect-ratio: auto; 
    height: 380px; 
    margin-bottom: 2rem; 
}

#sbsr-298 .cs-picture {
    width: 100%;
    height: 90%;
    margin-top: 6%;
}

#sbsr-298 .cs-picture img {
    height: 100%;
    object-fit: cover;
    object-position: center center; /* центрируем по вертикали */
}

#sbsr-298 .cs-box {
    width: 7rem;
    height: 7rem;
    bottom: -1.5rem;
    left: -3%;
    bottom: -3%;
}

#sbsr-298 .cs-number {
    font-size: 2.5rem;
}

#sbsr-298 .cs-number:before {
    width: 7rem;
    height: 7rem;
}
#sbsr-298 .cs-number::before {
    width: 96%;
    height: 96%;
}

</style>