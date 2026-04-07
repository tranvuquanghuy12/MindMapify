import { useState, useEffect, useMemo } from 'react'
import axios from 'axios'
import './App.css'
import ForceGraph from './components/ForceGraph'
import { Sparkles, Search, Box, X, Filter } from 'lucide-react'
import { motion, AnimatePresence } from 'framer-motion'

function App() {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedUnit, setSelectedUnit] = useState('All')
  const [datasetMode, setDatasetMode] = useState('grade8') // 'grade8' hoặc 'daily'
  const [fullData, setFullData] = useState({ nodes: [], links: [] })
  const [loading, setLoading] = useState(false)
  const [selectedNode, setSelectedNode] = useState(null)
  const [imageUrl, setImageUrl] = useState(null)

  useEffect(() => {
    const fetchGraph = async () => {
      setLoading(true)
      try {
        const response = await axios.get(`http://localhost:8000/graph?mode=${datasetMode}`)
        setFullData(response.data)
        setSelectedUnit('All') // Reset unit khi đổi mode
      } catch (error) {
        console.error('Lỗi khi tải bản đồ:', error)
      } finally {
        setLoading(false)
      }
    }
    fetchGraph()
  }, [datasetMode])

  // Danh sách các Unit duy nhất
  const units = useMemo(() => {
    const unitSet = new Set(fullData.nodes.map(n => n.unit))
    return ['All', ...Array.from(unitSet).sort()]
  }, [fullData])

  const filteredData = useMemo(() => {
    let nodes = fullData.nodes
    
    // Lọc theo Unit
    if (selectedUnit !== 'All') {
      nodes = nodes.filter(n => n.unit === selectedUnit)
    }

    // Lọc theo tìm kiếm
    if (searchTerm) {
      const term = searchTerm.toLowerCase()
      nodes = nodes.filter(n => 
        n.label.toLowerCase().includes(term) || 
        n.definition_vn?.toLowerCase().includes(term)
      )
    }

    const matchedNodeIds = new Set(nodes.map(n => n.id))
    const links = fullData.links.filter(l => 
      matchedNodeIds.has(l.source) && matchedNodeIds.has(l.target)
    )
    
    return { nodes, links }
  }, [searchTerm, selectedUnit, fullData])

  const handleNodeClick = async (node) => {
    setSelectedNode(node)
    setImageUrl(null)
    try {
      const response = await axios.post(`http://localhost:8000/generate-image?keyword=${node.label}`)
      setImageUrl(response.data.image_url)
    } catch (error) {
      console.error('Lỗi khi tải ảnh:', error)
    }
  }

  return (
    <div className="app-container">
      <header className="header">
        <div className="logo">
          <div className="logo-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
            </svg>
          </div>
          <h1>
            Semantic Visual Explorer 
            <span className="mode-badge">
              {datasetMode === 'grade8' ? 'Grade 8 Edition' : 'Daily & AI Edition'}
            </span>
          </h1>
        </div>
        
        <div className="unit-tabs">
          <button 
            className={`unit-tab ${datasetMode === 'grade8' ? 'active' : ''}`}
            onClick={() => setDatasetMode('grade8')}
          >
            Sách giáo khoa Lớp 8
          </button>
          <button 
            className={`unit-tab ${datasetMode === 'daily' ? 'active' : ''}`}
            onClick={() => setDatasetMode('daily')}
          >
            Giao tiếp & AI (1000+ từ)
          </button>
        </div>

        {datasetMode === 'grade8' && (
          <div className="unit-tabs">
            {units.map(unit => (
              <button 
                key={unit}
                className={`unit-tab ${selectedUnit === unit ? 'active' : ''}`}
                onClick={() => setSelectedUnit(unit)}
              >
                {unit}
              </button>
            ))}
          </div>
        )}

        <div style={{ display: 'flex', gap: '20px', color: 'rgba(255,255,255,0.4)', fontSize: '0.8rem' }}>
          <span>{filteredData.nodes.length} / {fullData.nodes.length} Từ vựng</span>
        </div>
      </header>

      <main className="graph-container">
        {loading ? (
          <div className="status-message">Đang tải dữ liệu từ điển...</div>
        ) : fullData.nodes.length === 0 ? (
          <div className="status-message">
            <p>Không tìm thấy dữ liệu đồ thị.</p>
          </div>
        ) : (
          <ForceGraph 
            data={filteredData} 
            onNodeClick={handleNodeClick} 
          />
        )}
      </main>

      <div className="input-section">
        <div className="search-container">
          <Search size={20} style={{ marginLeft: '12px', opacity: 0.4 }} />
          <input 
            type="text" 
            placeholder="Tìm kiếm từ vựng hoặc nghĩa tiếng Việt..." 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          {searchTerm && (
            <button 
              onClick={() => setSearchTerm('')} 
              style={{ background: 'transparent', padding: '0 1rem' }}
            >
              <X size={18} color="rgba(255,255,255,0.4)" />
            </button>
          )}
        </div>
      </div>

      <AnimatePresence>
        {selectedNode && (
          <motion.div 
            initial={{ opacity: 0, scale: 0.9, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.9, y: 20 }}
            className="flashcard-popup"
          >
            <div className="flashcard-header">
              <div>
                <h3 style={{ textTransform: 'capitalize', margin: 0 }}>{selectedNode.label}</h3>
                <code style={{ color: '#b983ff', fontSize: '0.9rem' }}>{selectedNode.pronunciation}</code>
              </div>
              <button onClick={() => setSelectedNode(null)} className="close-btn">✕</button>
            </div>

            <div className="flashcard-image">
              {imageUrl ? (
                <img src={imageUrl} alt={selectedNode.label} />
              ) : (
                <Sparkles className="animate-pulse" color="#00f2fe" size={32} />
              )}
            </div>

            <div className="flashcard-content">
              <p className="definition-vn">{selectedNode.definition_vn}</p>
              <div className="node-meta">
                <span className="badge-type">{selectedNode.type}</span>
                <span className="badge-unit">{selectedNode.unit}</span>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

export default App
