import { useCallback, useRef, useEffect } from 'react'
import ForceGraph2D from 'react-force-graph-2d'

const ForceGraph = ({ data, onNodeClick }) => {
  const fgRef = useRef()

  const hasZoomed = useRef(false)

  useEffect(() => {
    if (fgRef.current && data.nodes.length > 0 && !hasZoomed.current) {
      setTimeout(() => {
        fgRef.current.zoomToFit(400, 100)
        hasZoomed.current = true
      }, 500)
    }
  }, [data])

  const paintNode = useCallback((node, ctx, globalScale) => {
    const label = node.label || ''
    const fontSize = Math.max(12 / globalScale, 4) // Giới hạn kích thước font tối thiểu
    ctx.font = `${fontSize}px Inter, sans-serif`
    
    const textWidth = ctx.measureText(label).width
    const bckgDimensions = [textWidth, fontSize].map(n => n + fontSize * 0.5)

    const x = node.x || 0
    const y = node.y || 0
    const w = bckgDimensions[0]
    const h = bckgDimensions[1]

    // Vẽ nền cho node
    ctx.fillStyle = 'rgba(185, 131, 255, 0.15)'
    ctx.fillRect(x - w / 2, y - h / 2, w, h)
    
    // Vẽ viền
    ctx.strokeStyle = '#b983ff'
    ctx.lineWidth = 1 / globalScale
    ctx.strokeRect(x - w / 2, y - h / 2, w, h)

    // Vẽ chữ
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    ctx.fillStyle = '#ffffff'
    ctx.fillText(label, x, y)

    node.__bckgDimensions = bckgDimensions
  }, [])

  return (
    <div style={{ width: '100%', height: '100%', background: '#0a0a0c', overflow: 'hidden' }}>
      <ForceGraph2D
        ref={fgRef}
        graphData={data}
        width={window.innerWidth}
        height={window.innerHeight - 80} // Trừ đi chiều cao header
        nodeRelSize={6}
        nodeCanvasObject={paintNode}
        nodePointerAreaPaint={(node, color, ctx) => {
          ctx.fillStyle = color
          const bckgDimensions = node.__bckgDimensions
          if (bckgDimensions) {
            ctx.fillRect(node.x - bckgDimensions[0] / 2, node.y - bckgDimensions[1] / 2, bckgDimensions[0], bckgDimensions[1])
          }
        }}
        linkWidth={1.5}
        linkColor={() => 'rgba(255,255,255,0.08)'}
        linkDirectionalParticles={1}
        linkDirectionalParticleSpeed={0.005}
        backgroundColor="#0a0a0c"
        onNodeClick={onNodeClick}
        cooldownTicks={100}
      />
    </div>
  )
}

export default ForceGraph
