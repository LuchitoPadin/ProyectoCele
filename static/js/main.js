/**
 * =============================================================================
 * LÓGICA INTERACTIVA: CRÓNICA DE LA PRISA LIMEÑA
 * Diseñado para la cátedra de Comunicación Audiovisual
 * =============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initReadingProgress();
  initAmbientAudio();
  initSociologicalCalculator();
  initReferencesSearch();
  initScrollReveal();
});

/* =============================================================================
 * 1. BARRA DE PROGRESO DE LECTURA NARRATIVA
 * ============================================================================= */
function initReadingProgress() {
  const progressBar = document.getElementById('reading-progress');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (window.scrollY / totalHeight) * 100;
    progressBar.style.width = `${Math.min(100, Math.max(0, progress))}%`;
  }, { passive: true });
}

/* =============================================================================
 * 2. PAISAJE SONORO AMBIENTAL LIMEÑO (Web Audio API)
 * Simula el rumor sutil de garúa costera y tráfico nocturno distante.
 * ============================================================================= */
let audioCtx = null;
let isAudioPlaying = false;
let rainNoiseNode = null;
let trafficHumNode = null;
let masterGainNode = null;

function initAmbientAudio() {
  const toggleBtn = document.getElementById('audio-toggle-btn');
  if (!toggleBtn) return;

  toggleBtn.addEventListener('click', () => {
    if (!isAudioPlaying) {
      startAmbientSound(toggleBtn);
    } else {
      stopAmbientSound(toggleBtn);
    }
  });
}

function startAmbientSound(btn) {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!audioCtx) {
      audioCtx = new AudioContext();
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }

    masterGainNode = audioCtx.createGain();
    masterGainNode.gain.setValueAtTime(0.01, audioCtx.currentTime);
    masterGainNode.gain.exponentialRampToValueAtTime(0.12, audioCtx.currentTime + 2);
    masterGainNode.connect(audioCtx.destination);

    // 1. Sintetizador de Garúa / Lluvia suave (Ruido rosa filtrado)
    const bufferSize = audioCtx.sampleRate * 2;
    const noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
    const output = noiseBuffer.getChannelData(0);
    let b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
    
    for (let i = 0; i < bufferSize; i++) {
      const white = Math.random() * 2 - 1;
      b0 = 0.99886 * b0 + white * 0.0555179;
      b1 = 0.99332 * b1 + white * 0.0750759;
      b2 = 0.96900 * b2 + white * 0.1538520;
      b3 = 0.86650 * b3 + white * 0.3104856;
      b4 = 0.55000 * b4 + white * 0.5329522;
      b5 = -0.7616 * b5 - white * 0.0168980;
      output[i] = b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362;
      output[i] *= 0.04;
      b6 = white * 0.115926;
    }

    rainNoiseNode = audioCtx.createBufferSource();
    rainNoiseNode.buffer = noiseBuffer;
    rainNoiseNode.loop = true;

    // Filtro pasa-bajos para simular la humedad y la garúa amortiguada
    const rainFilter = audioCtx.createBiquadFilter();
    rainFilter.type = 'lowpass';
    rainFilter.frequency.value = 1100;

    rainNoiseNode.connect(rainFilter);
    rainFilter.connect(masterGainNode);
    rainNoiseNode.start();

    // 2. Rumor distante de baja frecuencia (Tráfico nocturno de la Vía Expresa)
    trafficHumNode = audioCtx.createOscillator();
    const trafficFilter = audioCtx.createBiquadFilter();
    const trafficGain = audioCtx.createGain();

    trafficHumNode.type = 'sine';
    trafficHumNode.frequency.setValueAtTime(65, audioCtx.currentTime); // 65 Hz rumor urbano
    trafficFilter.type = 'bandpass';
    trafficFilter.frequency.value = 90;
    trafficGain.gain.value = 0.06;

    trafficHumNode.connect(trafficFilter);
    trafficFilter.connect(trafficGain);
    trafficGain.connect(masterGainNode);
    trafficHumNode.start();

    isAudioPlaying = true;
    btn.classList.add('playing');
    const label = btn.querySelector('.audio-label');
    if (label) label.textContent = 'Ambiente Sonoro: Activo';
  } catch (err) {
    console.warn('Error al iniciar audio web:', err);
  }
}

function stopAmbientSound(btn) {
  if (masterGainNode && audioCtx) {
    masterGainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 1);
    setTimeout(() => {
      if (rainNoiseNode) {
        try { rainNoiseNode.stop(); } catch(e){}
      }
      if (trafficHumNode) {
        try { trafficHumNode.stop(); } catch(e){}
      }
      isAudioPlaying = false;
      btn.classList.remove('playing');
      const label = btn.querySelector('.audio-label');
      if (label) label.textContent = 'Sonido Ambiente: Inactivo';
    }, 1000);
  }
}

/* =============================================================================
 * 3. CALCULADORA SOCIOLÓGICA CONECTADA AL BACKEND FLASK
 * ============================================================================= */
function initSociologicalCalculator() {
  const form = document.getElementById('calc-form');
  const sliderTransporte = document.getElementById('slider-transporte');
  const valTransporte = document.getElementById('val-transporte');
  const sliderPantalla = document.getElementById('slider-pantalla');
  const valPantalla = document.getElementById('val-pantalla');
  const selectOcupacion = document.getElementById('select-ocupacion');

  if (!form || !sliderTransporte || !sliderPantalla) return;

  // Actualización visual de etiquetas de rangos
  sliderTransporte.addEventListener('input', (e) => {
    valTransporte.textContent = `${parseFloat(e.target.value).toFixed(1)} hrs/día`;
  });

  sliderPantalla.addEventListener('input', (e) => {
    valPantalla.textContent = `${parseFloat(e.target.value).toFixed(1)} hrs/día`;
  });

  // Envío al backend Flask via Fetch API
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = document.getElementById('btn-submit-calc');
    const originalText = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = '<span>Calculando impacto...</span>';

    const payload = {
      horas_transporte: parseFloat(sliderTransporte.value),
      horas_pantalla: parseFloat(sliderPantalla.value),
      ocupacion: selectOcupacion ? selectOcupacion.value : 'universitario'
    };

    try {
      const response = await fetch('/api/calcular-tiempo', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (!response.ok) throw new Error('Error en el servidor');
      const data = await response.json();
      renderCalculatorResults(data);
    } catch (err) {
      console.error('Error calculando:', err);
      // Fallback local si el servidor tiene algún retraso momentáneo
      renderFallbackResults(payload);
    } finally {
      btn.disabled = false;
      btn.innerHTML = originalText;
    }
  });
}

function renderCalculatorResults(data) {
  const panel = document.getElementById('calc-results');
  if (!panel) return;

  panel.innerHTML = `
    <div class="calc-result-header">
      <h4>Diagnóstico Sociológico Individual</h4>
      <div class="calc-risk-badge">${data.nivel_alerta}</div>
    </div>
    
    <div class="calc-stats-grid">
      <div class="calc-stat-item">
        <div class="calc-stat-val">${data.dias_perdidos_anual_en_trafico} <span style="font-size: 1rem; color: var(--text-dim);">días/año</span></div>
        <div class="calc-stat-desc">Tiempo de vida absorbido íntegramente por el tráfico limeño.</div>
      </div>
      <div class="calc-stat-item">
        <div class="calc-stat-val">${data.horas_afectivas_diarias_reales} <span style="font-size: 1rem; color: var(--text-dim);">hrs/día</span></div>
        <div class="calc-stat-desc">Ventana neta de presencia y escucha afectiva sin pantallas.</div>
      </div>
      <div class="calc-stat-item">
        <div class="calc-stat-val">${data.riesgo_spillover_porcentaje}%</div>
        <div class="calc-stat-desc">Vulnerabilidad al fenómeno Spillover (derrame de fatiga laboral).</div>
      </div>
      <div class="calc-stat-item">
        <div class="calc-stat-val">${data.horas_anuales_en_trafico} <span style="font-size: 1rem; color: var(--text-dim);">hrs</span></div>
        <div class="calc-stat-desc">Horas anuales no recuperables en el transporte público.</div>
      </div>
    </div>

    <div class="calc-diagnosis-text">
      <strong>Lectura crítica:</strong> ${data.diagnostico}
    </div>

    <div class="calc-strategy-text">
      <strong>Pauta recomendada del informe:</strong> ${data.estrategia_sugerida}
    </div>
  `;
}

function renderFallbackResults(payload) {
  const dias = ((payload.horas_transporte * 260) / 24).toFixed(1);
  const panel = document.getElementById('calc-results');
  if (!panel) return;
  panel.innerHTML = `
    <div class="calc-result-header">
      <h4>Diagnóstico Sociológico (Procesado)</h4>
      <div class="calc-risk-badge">Alerta de Sobrecarga Urbana</div>
    </div>
    <div class="calc-stats-grid">
      <div class="calc-stat-item">
        <div class="calc-stat-val">${dias} días/año</div>
        <div class="calc-stat-desc">Equivalente de tiempo absorbido en el tráfico de Lima.</div>
      </div>
    </div>
  `;
}

/* =============================================================================
 * 4. BÚSQUEDA Y FILTRADO DE REFERENCIAS BIBLIOGRÁFICAS (APA 7)
 * ============================================================================= */
function initReferencesSearch() {
  const searchInput = document.getElementById('ref-search');
  const refItems = document.querySelectorAll('.reference-item');

  if (!searchInput || !refItems.length) return;

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    refItems.forEach(item => {
      const text = item.textContent.toLowerCase();
      if (text.includes(query)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  });
}

/* =============================================================================
 * 5. ANIMACIONES SUTILES AL SCROLL (Intersection Observer)
 * ============================================================================= */
function initScrollReveal() {
  const observerOptions = {
    threshold: 0.12,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.metric-card, .chronicle-item, .concept-card, .pauta-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1)';
    observer.observe(el);
  });
}

// Inyectar clase revealed
const style = document.createElement('style');
style.textContent = `
  .revealed {
    opacity: 1 !important;
    transform: translateY(0) !important;
  }
`;
document.head.appendChild(style);
