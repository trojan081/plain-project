<template>
<section id="services-1188">
    <div class="cs-container">
        <div class="cs-content">
            <h2 class="cs-title">Используй преимущества Plain</h2>
        </div>
        <ul class="cs-card-group">
            <li class="cs-item">
                <picture class="cs-picture">
                    <img class="cs-icon"
                            src="/public/assets/adv_1.2.png"
                            loading="lazy" decoding="async" alt="icon" width="33" height="38" aria-hidden="true">
                </picture>
                <!-- Text Grouped For Flexbox-->
                <div class="cs-text-group">
                    <h3 class="cs-h3">Скорость: забудьте про дедлайны</h3>
                    <p class="cs-item-text">Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                </div>
            </li>
            <li class="cs-item">
                <picture class="cs-picture">
                    <img class="cs-icon" src="/public/assets/adv_2.1.png"
                            loading="lazy" decoding="async" alt="icon" width="33" height="38" aria-hidden="true">
                </picture>
                <!-- Text Grouped For Flexbox-->
                <div class="cs-text-group">
                    <h3 class="cs-h3">Brake Repair Service</h3>
                    <p class="cs-item-text">Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                </div>
            </li>
            <li class="cs-item">
                <picture class="cs-picture">
                    <img class="cs-icon"
                            src="/public/assets/adv_3.1.png"
                            loading="lazy" decoding="async" alt="icon" width="33" height="38" aria-hidden="true">
                </picture>
                <!-- Text Grouped For Flexbox-->
                <div class="cs-text-group">
                    <h3 class="cs-h3">AC Repair Service</h3>
                    <p class="cs-item-text">Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                </div>
            </li>
            <li class="cs-item">
                <picture class="cs-picture">
                    <img class="cs-icon"
                            src="/public/assets/adv_4.1.png" loading="lazy"
                            decoding="async" alt="icon" width="33" height="38" aria-hidden="true">
                </picture>
                <!-- Text Grouped For Flexbox-->
                <div class="cs-text-group">
                    <h3 class="cs-h3">Oil Filter Change</h3>
                    <p class="cs-item-text">Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                </div>
            </li>
            <li class="cs-item">
                <picture class="cs-picture">
                    <img class="cs-icon"
                            src="/public/assets/adv_5.1.png" loading="lazy"
                            decoding="async" alt="icon" width="33" height="38" aria-hidden="true">
                </picture>
                <!-- Text Grouped For Flexbox-->
                <div class="cs-text-group">
                    <h3 class="cs-h3">Changing Wheel</h3>
                    <p class="cs-item-text">Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                </div>
            </li>
            <li class="cs-item">
                <picture class="cs-picture">
                    <img class="cs-icon"
                            src="/public/assets/adv_6.1.png"
                            loading="lazy" decoding="async" alt="icon" width="33" height="38" aria-hidden="true">
                </picture>
                <!-- Text Grouped For Flexbox-->
                <div class="cs-text-group">
                    <h3 class="cs-h3">Emissions Repair</h3>
                    <p class="cs-item-text">Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                </div>
            </li>
        </ul>
        <a href="" class="cs-button-solid">Book Appointment</a>
    </div>
</section>
</template>                        

<style scoped>

/*-- -------------------------- -->
<---          Services          -->
<--- -------------------------- -*/
/* Mobile - 360px */
@media only screen and (min-width: 0rem) {
    #services-1188 {
        padding: var(--sectionPadding);
    }
    #services-1188 .cs-container {
        max-width: 80rem;
        width: 100%;
        margin: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        /* 48px - 64px */
        gap: clamp(3rem, 6vw, 4rem);
    }
    #services-1188 .cs-content {
        width: 100%;
        display: flex;
        flex-direction: column;
        /* centers content horizontally, set to flex-start to left align */
        align-items: center;
        /* set text align to left if content needs to be left aligned */
        text-align: center;
    }

    #services-1188 .cs-card-group {
        /* changes to 1280px at desktop */
        max-width: 56.25rem;
        width: 100%;
        margin: 0;
        padding: 0;
        display: grid;
        justify-content: center;
        gap: 1rem;
    }
    #services-1188 .cs-item {
        list-style: none;
        max-width: 23rem;
        width: 100%;
        margin: 0;
        box-sizing: border-box;
        padding: 1rem;
        border: 1px solid #e8e8e8;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: left;
    }
    #services-1188 .cs-picture {
        width: 5rem;
        height: 5rem;
        margin-bottom: 1.25rem;
        box-sizing: border-box;
        /* prevents border from affecting height and width */
        background-color: #f7f7f7;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        /* prevents flexbox from squishing it */
        flex: none;
    }
    #services-1188 .cs-icon {
        width: 6.875rem;
        height: auto;
        display: block;
        border-radius: 100px;
    }
    #services-1188 .cs-h3 {
        font-size: 1.25rem;
        line-height: 1.5em;
        margin: 0;
        margin-bottom: 0.5rem;
        color: var(--headerColor);
        text-align: center;
    }
    #services-1188 .cs-item-text {
        /* 14px - 16px */
        font-size: clamp(0.875rem, 1.5vw, 1rem);
        line-height: 1.5em;
        margin: 0;
        color: var(--bodyTextColor);
        text-align: center;
    }
    #services-1188 .cs-button-solid {
        font-size: 1rem;
        /* 46px - 56px */
        line-height: clamp(2.875rem, 5.5vw, 3.5rem);
        font-weight: 700;
        min-width: 9.375rem;
        margin: 0;
        /* prevents padding from adding to the width */
        box-sizing: border-box;
        padding: 0 1.5rem;
        color: #fff;
        background-color: var(--primary);
        text-decoration: none;
        display: inline-block;
        position: relative;
        z-index: 1;
        text-align: center;
    }
    #services-1188 .cs-button-solid:before {
        content: "";
        width: 0%;
        height: 100%;
        background: #000;
        opacity: 1;
        border-radius: 0.25rem;
        position: absolute;
        top: 0;
        left: 0;
        z-index: -1;
        transition: width 0.3s;
    }
    #services-1188 .cs-button-solid:hover:before {
        width: 100%;
    }
}
/* Tablet - 768px */
@media only screen and (min-width: 48rem) {
    #services-1188 .cs-card-group {
        grid-template-columns: repeat(3, 1fr);
        gap: 1.25rem;
    }
    #services-1188 .cs-item {
        margin: 0;
    }
}
/* Large Desktop - 1300px */
@media only screen and (min-width: 81.25rem) {
    #services-1188 .cs-card-group {
        max-width: 80rem;
    }
    #services-1188 .cs-item {
        max-width: none;
        padding: 2rem 1.5rem;
    }
}
.cs-title {
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  font-size: clamp(0.8rem, 4vw + 0.5rem, 2.8rem);
  font-weight: 600;
  color: #333;
  margin-bottom: 1rem;
  line-height: 1.2;
}
                                
</style>