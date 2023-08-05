function startAutoSlider() {
    const slides = document.querySelectorAll('.slide');
    let slideIndex = 0;
  
    function showSlide(index) {
      slides.forEach((slide, i) => {
        slide.style.display = i === index ? 'flex' : 'none';
      });
    }
  
    function nextSlide() {
      slideIndex = (slideIndex + 1) % slides.length;
      showSlide(slideIndex);
    }
  
    // Show the first slide
    showSlide(slideIndex);
  
    // Automatically switch slides every 5 seconds
    setInterval(nextSlide, 5000);
  }
  
  // Start the auto slider
  startAutoSlider();
  